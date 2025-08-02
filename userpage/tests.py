from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm

# 🔐 Authentication Tests
class AuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.profile_url = reverse('profile')

    def test_register_user(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to login
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login_user(self):
        User.objects.create_user(username='testuser', password='StrongPass123!')
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'StrongPass123!'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to profile

# 👤 Profile View and Update Tests
class ProfileTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='StrongPass123!')
        self.profile, _ = Profile.objects.get_or_create(user=self.user)
        self.profile_url = reverse('profile')
        self.update_url = reverse('update_profile')

    def test_profile_view_requires_login(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_profile_view_authenticated(self):
        self.client.login(username='testuser', password='StrongPass123!')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)

    def test_update_profile(self):
        self.client.login(username='testuser', password='StrongPass123!')
        response = self.client.post(self.update_url)
        self.assertEqual(response.status_code, 302)  # ✅ Expect redirect to profile
        self.profile.refresh_from_db()

# ❌ Delete Profile Tests
class DeleteProfileTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='StrongPass123!')
        self.profile, _ = Profile.objects.get_or_create(user=self.user)
        self.delete_url = reverse('delete_profile')

    def test_delete_profile(self):
        self.client.login(username='testuser', password='StrongPass123!')
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)  # Redirect to register
        self.assertFalse(User.objects.filter(username='testuser').exists())
        self.assertFalse(Profile.objects.filter(user=self.user).exists())

# ✅ Form Validation Tests
def test_profile_form_valid(self):
    user = User.objects.create_user(username='formuser', password='StrongPass123!')
    profile, _ = Profile.objects.get_or_create(user=user)

    form = ProfileForm(data={}, instance=profile)

    self.assertTrue(form.is_valid())