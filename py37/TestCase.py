import unittest
import Constants
import TBot


class TestCase(unittest.TestCase):
    """Class contains a lot of unit tests for classes: Token, BotHandler."""

    def test_get_updates(self):
        result = TBot.BotHandler(Constants.Token()).get_updates()
        self.assertEqual(result['ok'], True)

    def test_send_message(self):
        bot = TBot.BotHandler(Constants.Token())
        result = '200' in str(bot.send_message(bot.get_chat_id(), 'Test message to personal Bot!'))
        self.assertEqual(result, True)

    def test_get_last_update(self):
        result = TBot.BotHandler(Constants.Token()).get_last_update()
        self.assertNotEqual(len(result), 0)

    def test_get_chat_id(self):
        result = TBot.BotHandler(Constants.Token()).get_chat_id()
        self.assertIsNotNone(result)
