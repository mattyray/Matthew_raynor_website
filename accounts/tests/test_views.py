from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from store.models import Order, Review, Product

User = get_user_model()

class SignupViewTest(TestCase):
    def test_get_signup_page(self):
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'account/signup.html')

    def test_post_signup_creates_user_and_redirects(self):
        data = {
            'email': 'view@user.com',
            'password1': 'Pass!2345',
            'password2': 'Pass!2345'
        }
        resp = self.client.post(reverse('signup'), data)
        self.assertRedirects(resp, reverse('account_login'))
        self.assertTrue(User.objects.filter(email='view@user.com').exists())

class LogoutViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='lo@user.com', password='xyz123')
        self.client.login(email='lo@user.com', password='xyz123')

    def test_custom_logout(self):
        resp = self.client.get(reverse('logout'))
        self.assertRedirects(resp, '/')
        # now anonymous
        resp2 = self.client.get(reverse('dashboard'))
        self.assertRedirects(resp2, '/accounts/login/?next=/accounts/dashboard/')

class DashboardViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='dash@user.com', password='dash123')
        self.client.login(email='dash@user.com', password='dash123')
        # create some orders and reviews
        Order.objects.create(customer_email='dash@user.com', status='P')

        product = Product.objects.create(
            product_type='book',
            title='Test Product',
            description='Test description',
            price=10.00,
            stock=5
        )

        Review.objects.create(user=self.user, product=product, comment='ok', rating=5)

    def test_dashboard_context(self):
        resp = self.client.get(reverse('dashboard'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('orders', resp.context)
        self.assertIn('reviews', resp.context)

class ProfileEditViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='edit@user.com', password='ed!t123')
        self.client.login(email='edit@user.com', password='ed!t123')

    def test_get_profile_edit(self):
        resp = self.client.get(reverse('profile_edit'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'account/profile_edit.html')

    def test_post_profile_edit_updates_user(self):
        resp = self.client.post(reverse('profile_edit'), {'email': 'newemail@user.com'})
        self.assertRedirects(resp, reverse('dashboard'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'newemail@user.com')
