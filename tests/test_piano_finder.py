from httpx import Response
import respx
from unittest.mock import MagicMock, patch

from enums import Pianos
from main import main
from piano_seeker import PianoFinder, PIANO_PAGES_MAPPING
from tests.fixtures.mocks import RESULTS_FOR_PIANO


class TestPianoFinder:

    @patch.object(PianoFinder, "get_offers")
    def test_piano_finder_returns_number_of_offers(self, finder_mock: MagicMock):
        main()
        assert finder_mock.call_count == 5

    def test_returns_offer(self, respx_mock: respx.MockRouter):
        respx_mock.get(
            PIANO_PAGES_MAPPING[Pianos.YAMAHA_CP_60_M.value]
        ).mock(return_value=Response(200, text=str(RESULTS_FOR_PIANO)))
        response = PianoFinder(Pianos.YAMAHA_CP_60_M.value).get_offers()
        assert response == RESULTS_FOR_PIANO
