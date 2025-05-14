#!/bin/bash

(
  echo "===== Docker & Deployment ====="
  cat Dockerfile
  echo
  cat docker-compose.yml
  echo
  cat docker-compose-prod.yml
  echo
  cat heroku.yml
  echo
  cat Procfile

  echo -e "\n\n===== Requirements ====="
  cat requirements.txt
  echo
  cat requirements-dev.txt

  echo -e "\n\n===== manage.py ====="
  cat manage.py

  echo -e "\n\n===== Django Settings ====="
  for file in base.py dev.py prod.py test.py __init__.py; do
    echo -e "\n===== django_project/settings/$file ====="
    cat django_project/settings/$file
  done

  echo -e "\n\n===== django_project config files ====="
  for file in urls.py wsgi.py asgi.py; do
    echo -e "\n===== django_project/$file ====="
    cat django_project/$file
  done

  for app in accounts pages blog portfolio store chat; do
    echo -e "\n\n===== APP: $app ====="
    for file in models.py views.py forms.py urls.py admin.py; do
      if [ -f $app/$file ]; then
        echo -e "\n===== $app/$file ====="
        cat $app/$file
      fi
    done

    if [ -f $app/tests.py ]; then
      echo -e "\n===== $app/tests.py ====="
      cat $app/tests.py
    fi

    find $app/tests -type f -name "*.py" | while read testfile; do
      echo -e "\n===== $testfile ====="
      cat "$testfile"
    done

    echo -e "\n== $app/migrations (filenames only) =="
    find $app/migrations -type f -name "*.py" | grep -v "__init__" || echo "None"
  done

  # === Include special chat app files ===
  echo -e "\n\n===== chat/utils.py ====="
  cat chat/utils.py

  echo -e "\n\n===== chat/openai_utils.py ====="
  cat chat/openai_utils.py

  echo -e "\n\n===== chat/knowledge_base.py ====="
  cat chat/knowledge_base.py

  echo -e "\n\n===== chat/data/*.json ====="
  find chat/data -type f -name "*.json" | while read jsonfile; do
    echo -e "\n===== $jsonfile ====="
    cat "$jsonfile"
  done

  echo -e "\n\n===== Templates ====="
  find templates -type f -name "*.html" | while read tmpl; do
    echo -e "\n===== $tmpl ====="
    cat "$tmpl"
  done

  echo -e "\n\n===== SCSS Files ====="
  find static -type f -name "*.scss" | while read scssfile; do
    echo -e "\n===== $scssfile ====="
    cat "$scssfile"
  done

  echo -e "\n\n===== README.md ====="
  cat README.md

) > project_code_output.txt
