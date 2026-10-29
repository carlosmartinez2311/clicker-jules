import pathlib
import unittest
from playwright.sync_api import sync_playwright

class TestCookieClickerAchievements(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)
        html_path = pathlib.Path(__file__).parent.parent / "index.html"
        cls.url = f"file://{html_path.resolve()}"

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def setUp(self):
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def tearDown(self):
        self.context.close()

    def test_initial_state_all_locked(self):
        self.page.goto(self.url)
        self.assertEqual(self.page.inner_text('#counter'), '0')

        # All trophies should be locked initially
        self.assertNotIn('unlocked', self.page.get_attribute('#trophy-10', 'class') or '')
        self.assertNotIn('unlocked', self.page.get_attribute('#trophy-100', 'class') or '')
        self.assertNotIn('unlocked', self.page.get_attribute('#trophy-1000', 'class') or '')

        self.assertEqual(self.page.inner_text('#badge-10'), 'Locked')
        self.assertEqual(self.page.inner_text('#badge-100'), 'Locked')
        self.assertEqual(self.page.inner_text('#badge-1000'), 'Locked')

    def test_unlock_10_clicks_bronze_trophy(self):
        self.page.goto(self.url)
        cookie = self.page.locator('#cookie')

        # Click 10 times
        for _ in range(10):
            cookie.click()

        self.assertEqual(self.page.inner_text('#counter'), '10')
        self.assertIn('unlocked', self.page.get_attribute('#trophy-10', 'class'))
        self.assertEqual(self.page.inner_text('#badge-10'), 'Unlocked!')

        # 100 and 1000 should still be locked
        self.assertNotIn('unlocked', self.page.get_attribute('#trophy-100', 'class') or '')
        self.assertNotIn('unlocked', self.page.get_attribute('#trophy-1000', 'class') or '')

        # Toast notification should be visible
        toast = self.page.locator('.toast')
        self.assertTrue(toast.is_visible())
        self.assertIn('Bronze Trophy', toast.inner_text())

    def test_unlock_100_and_1000_clicks(self):
        self.page.goto(self.url)

        # Simulate reaching 99 clicks via localStorage
        self.page.evaluate("localStorage.setItem('cookieCount', 99)")
        self.page.reload()

        self.assertEqual(self.page.inner_text('#counter'), '99')
        self.assertIn('unlocked', self.page.get_attribute('#trophy-10', 'class'))
        self.assertNotIn('unlocked', self.page.get_attribute('#trophy-100', 'class') or '')

        # Click 100th time
        self.page.locator('#cookie').click()
        self.assertEqual(self.page.inner_text('#counter'), '100')
        self.assertIn('unlocked', self.page.get_attribute('#trophy-100', 'class'))
        self.assertEqual(self.page.inner_text('#badge-100'), 'Unlocked!')

        # Simulate reaching 999 clicks via localStorage
        self.page.evaluate("localStorage.setItem('cookieCount', 999)")
        self.page.reload()
        self.page.locator('#cookie').click()

        self.assertEqual(self.page.inner_text('#counter'), '1000')
        self.assertIn('unlocked', self.page.get_attribute('#trophy-1000', 'class'))
        self.assertEqual(self.page.inner_text('#badge-1000'), 'Unlocked!')

    def test_reset_counter_relocks_achievements(self):
        self.page.goto(self.url)

        # Set count to 100 and reload
        self.page.evaluate("localStorage.setItem('cookieCount', 100)")
        self.page.reload()
        self.assertIn('unlocked', self.page.get_attribute('#trophy-10', 'class'))
        self.assertIn('unlocked', self.page.get_attribute('#trophy-100', 'class'))

        # Accept confirmation dialog when clicking reset
        self.page.on('dialog', lambda dialog: dialog.accept())
        self.page.locator('#reset-btn').click()

        self.assertEqual(self.page.inner_text('#counter'), '0')
        self.assertNotIn('unlocked', self.page.get_attribute('#trophy-10', 'class') or '')
        self.assertNotIn('unlocked', self.page.get_attribute('#trophy-100', 'class') or '')
        self.assertEqual(self.page.inner_text('#badge-10'), 'Locked')
        self.assertEqual(self.page.inner_text('#badge-100'), 'Locked')


if __name__ == '__main__':
    unittest.main()
