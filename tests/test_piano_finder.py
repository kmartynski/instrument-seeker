from unittest.mock import MagicMock, patch

from piano_seeker import PianoFinder

from main import main


class TestPianoFinder:

    @patch.object(PianoFinder, "get_offers")
    def test_piano_finder_returns_offers(self, finder_mock: MagicMock):
        main()
        assert finder_mock.call_count == 5
