// chatwidget/static/chatwidget/js/chat.js

document.addEventListener("DOMContentLoaded", () => {
  const $chatToggle = document.getElementById("ai-chatbot-toggle");
  const $chatWidget = document.getElementById("ai-chatbot");
  const $chatInput = $chatWidget.querySelector("input");
  const $chatBody = document.getElementById("ai-chatbot-body");

  $chatToggle.addEventListener("click", () => {
    $chatWidget.style.display = "block";
    $chatInput.focus();
  });

  document.getElementById("ai-chatbot-close").addEventListener("click", () => {
    $chatWidget.style.display = "none";
  });

  $chatInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && $chatInput.value.trim() !== "") {
      const message = $chatInput.value;
      $chatInput.value = "";
      appendMessage("user", message);
      fetch("/chatwidget/api/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
      })
      .then(res => res.json())
      .then(data => {
        appendMessage("ai", data.reply || data.error || "⚠️ No reply");
      });
    }
  });

  function appendMessage(sender, text) {
    const msg = document.createElement("div");
    msg.className = `chat-message ${sender} fade-in`;
    msg.innerHTML = text;
    $chatBody.appendChild(msg);
    $chatBody.scrollTop = $chatBody.scrollHeight;
  }
});
