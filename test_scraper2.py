import unittest

from numpy import dtype
import scraper2

class ScraperLinksTestCase(unittest.TestCase):
    def setUp(self):
        self.bot = scraper2.Scraper('https://ftx.com/markets')
   
    def test_find_all_links(self):
        expected_original_find_all_links = ['https://about.ftx.com/', 'https://blog.ftx.com/', 'https://docs.ftx.com/', 'https://ftexchange.zendesk.com/hc/en-us', 
        'https://ftx.com/', 'https://ftx.com/apps', 'https://ftx.com/expired-futures', 'https://ftx.com/ftt', 'https://ftx.com/ftt', 
        'https://ftx.com/leaderboard', 'https://ftx.com/markets', 'https://ftx.com/markets/fiat', 'https://ftx.com/markets/future', 
        'https://ftx.com/markets/lt', 'https://ftx.com/markets/prediction', 'https://ftx.com/markets/recent', 'https://ftx.com/markets/spot', 
        'https://ftx.com/markets/volatility', 'https://ftx.com/nfts', 'https://ftx.com/onboarding/signup', 'https://ftx.com/support', 
        'https://ftx.com/support', 'https://ftx.com/support', 'https://ftx.com/trade/1INCH-0325', 'https://ftx.com/trade/1INCH-PERP', 
        'https://ftx.com/trade/AAVE-0325', 'https://ftx.com/trade/AAVE-PERP', 'https://ftx.com/trade/ADA-0325', 'https://ftx.com/trade/ADA-PERP', 
        'https://ftx.com/trade/AGLD-PERP', 'https://ftx.com/trade/ALCX-PERP', 'https://ftx.com/trade/ALGO-0325', 'https://ftx.com/trade/ALGO-PERP', 
        'https://ftx.com/trade/ALICE-PERP', 'https://ftx.com/trade/ALPHA-PERP', 'https://ftx.com/trade/ALT-0325', 'https://ftx.com/trade/ALT-PERP', 
        'https://ftx.com/trade/AMPL-PERP', 'https://ftx.com/trade/AR-PERP', 'https://ftx.com/trade/ASD-PERP', 'https://ftx.com/trade/ATLAS-PERP', 
        'https://ftx.com/trade/ATOM-0325', 'https://ftx.com/trade/ATOM-PERP', 'https://ftx.com/trade/AUDIO-PERP', 'https://ftx.com/trade/AVAX-0325', 
        'https://ftx.com/trade/AVAX-PERP', 'https://ftx.com/trade/AXS-PERP', 'https://ftx.com/trade/BADGER-PERP', 'https://ftx.com/trade/BAL-0325', 
        'https://ftx.com/trade/BAL-PERP', 'https://ftx.com/trade/BAND-PERP', 'https://ftx.com/trade/BAO-PERP', 'https://ftx.com/trade/BAT-PERP', 
        'https://ftx.com/trade/BCH-0325', 'https://ftx.com/trade/BCH-PERP', 'https://ftx.com/trade/BIT-PERP', 'https://ftx.com/trade/BNB-0325', 
        'https://ftx.com/trade/BNB-PERP', 'https://ftx.com/trade/BNT-PERP', 'https://ftx.com/trade/BOBA-PERP', 'https://ftx.com/trade/BRZ-PERP', 
        'https://ftx.com/trade/BSV-0325', 'https://ftx.com/trade/BSV-PERP', 'https://ftx.com/trade/BTC-0325', 'https://ftx.com/trade/BTC-0624', 
        'https://ftx.com/trade/BTC-PERP', 'https://ftx.com/trade/BTC-PERP', 'https://ftx.com/trade/BTT-PERP', 'https://ftx.com/trade/C98-PERP', 
        'https://ftx.com/trade/CAKE-PERP', 'https://ftx.com/trade/CEL-0325', 'https://ftx.com/trade/CEL-PERP', 'https://ftx.com/trade/CELO-PERP', 
        'https://ftx.com/trade/CHR-PERP', 'https://ftx.com/trade/CHZ-0325', 'https://ftx.com/trade/CHZ-PERP', 'https://ftx.com/trade/CLV-PERP', 
        'https://ftx.com/trade/COMP-0325', 'https://ftx.com/trade/COMP-PERP', 'https://ftx.com/trade/CONV-PERP', 'https://ftx.com/trade/CREAM-PERP', 
        'https://ftx.com/trade/CRO-PERP', 'https://ftx.com/trade/CRV-PERP', 'https://ftx.com/trade/CUSDT-PERP', 'https://ftx.com/trade/CVC-PERP', 
        'https://ftx.com/trade/DASH-PERP', 'https://ftx.com/trade/DAWN-PERP', 'https://ftx.com/trade/DEFI-0325', 'https://ftx.com/trade/DEFI-PERP', 
        'https://ftx.com/trade/DENT-PERP', 'https://ftx.com/trade/DODO-PERP', 'https://ftx.com/trade/DOGE-0325', 'https://ftx.com/trade/DOGE-PERP', 
        'https://ftx.com/trade/DOT-0325', 'https://ftx.com/trade/DOT-PERP', 'https://ftx.com/trade/DRGN-0325', 'https://ftx.com/trade/DRGN-PERP', 
        'https://ftx.com/trade/DYDX-PERP', 'https://ftx.com/trade/EDEN-0325', 'https://ftx.com/trade/EDEN-PERP', 'https://ftx.com/trade/EGLD-PERP', 
        'https://ftx.com/trade/ENJ-PERP', 'https://ftx.com/trade/ENS-PERP', 'https://ftx.com/trade/EOS-0325', 'https://ftx.com/trade/EOS-PERP', 
        'https://ftx.com/trade/ETC-PERP', 'https://ftx.com/trade/ETH-0325', 'https://ftx.com/trade/ETH-0624', 'https://ftx.com/trade/ETH-PERP', 
        'https://ftx.com/trade/ETH-PERP', 'https://ftx.com/trade/EXCH-0325', 'https://ftx.com/trade/EXCH-PERP', 'https://ftx.com/trade/FIDA-PERP', 
        'https://ftx.com/trade/FIL-0325', 'https://ftx.com/trade/FIL-PERP', 'https://ftx.com/trade/FLM-PERP', 'https://ftx.com/trade/FLOW-PERP', 
        'https://ftx.com/trade/FTM-PERP', 'https://ftx.com/trade/FTT-PERP', 'https://ftx.com/trade/FTT/USD', 'https://ftx.com/trade/GALA-PERP', 
        'https://ftx.com/trade/GRT-0325', 'https://ftx.com/trade/GRT-PERP', 'https://ftx.com/trade/HBAR-PERP', 'https://ftx.com/trade/HNT-PERP', 
        'https://ftx.com/trade/HOLY-PERP', 'https://ftx.com/trade/HOT-PERP', 'https://ftx.com/trade/HT-PERP', 'https://ftx.com/trade/HUM-PERP', 
        'https://ftx.com/trade/ICP-PERP', 'https://ftx.com/trade/ICX-PERP', 'https://ftx.com/trade/IMX-PERP', 'https://ftx.com/trade/IOTA-PERP', 
        'https://ftx.com/trade/KAVA-PERP', 'https://ftx.com/trade/KBTT-PERP', 'https://ftx.com/trade/KIN-PERP', 'https://ftx.com/trade/KNC-PERP', 
        'https://ftx.com/trade/KSHIB-PERP', 'https://ftx.com/trade/KSM-PERP', 'https://ftx.com/trade/KSOS-PERP', 'https://ftx.com/trade/LEO-PERP', 
        'https://ftx.com/trade/LINA-PERP', 'https://ftx.com/trade/LINK-0325', 'https://ftx.com/trade/LINK-PERP', 'https://ftx.com/trade/LOOKS-PERP', 
        'https://ftx.com/trade/LRC-PERP', 'https://ftx.com/trade/LTC-0325', 'https://ftx.com/trade/LTC-PERP', 'https://ftx.com/trade/LUNA-PERP', 
        'https://ftx.com/trade/MANA-PERP', 'https://ftx.com/trade/MAPS-PERP', 'https://ftx.com/trade/MATIC-PERP', 'https://ftx.com/trade/MCB-PERP', 
        'https://ftx.com/trade/MEDIA-PERP', 'https://ftx.com/trade/MER-PERP', 'https://ftx.com/trade/MID-0325', 'https://ftx.com/trade/MID-PERP', 
        'https://ftx.com/trade/MINA-PERP', 'https://ftx.com/trade/MKR-PERP', 'https://ftx.com/trade/MNGO-PERP', 'https://ftx.com/trade/MTA-PERP', 
        'https://ftx.com/trade/MTL-PERP', 'https://ftx.com/trade/MVDA10-PERP', 'https://ftx.com/trade/MVDA25-PERP', 'https://ftx.com/trade/NEAR-PERP', 
        'https://ftx.com/trade/NEO-PERP', 'https://ftx.com/trade/OKB-0325', 'https://ftx.com/trade/OKB-PERP', 'https://ftx.com/trade/OMG-0325', 
        'https://ftx.com/trade/OMG-PERP', 'https://ftx.com/trade/ONE-PERP', 'https://ftx.com/trade/ONT-PERP', 'https://ftx.com/trade/ORBS-PERP', 
        'https://ftx.com/trade/OXY-PERP', 'https://ftx.com/trade/PAXG-PERP', 'https://ftx.com/trade/PEOPLE-PERP', 'https://ftx.com/trade/PERP-PERP', 
        'https://ftx.com/trade/POLIS-PERP', 'https://ftx.com/trade/PRIV-0325', 'https://ftx.com/trade/PRIV-PERP', 'https://ftx.com/trade/PROM-PERP', 
        'https://ftx.com/trade/PUNDIX-PERP', 'https://ftx.com/trade/QTUM-PERP', 'https://ftx.com/trade/RAMP-PERP', 'https://ftx.com/trade/RAY-PERP', 
        'https://ftx.com/trade/REEF-0325', 'https://ftx.com/trade/REEF-PERP', 'https://ftx.com/trade/REN-PERP', 'https://ftx.com/trade/RNDR-PERP', 
        'https://ftx.com/trade/RON-PERP', 'https://ftx.com/trade/ROOK-PERP', 'https://ftx.com/trade/ROSE-PERP', 'https://ftx.com/trade/RSR-PERP', 
        'https://ftx.com/trade/RUNE-PERP', 'https://ftx.com/trade/SAND-PERP', 'https://ftx.com/trade/SC-PERP', 'https://ftx.com/trade/SCRT-PERP', 
        'https://ftx.com/trade/SECO-PERP', 'https://ftx.com/trade/SHIB-PERP', 'https://ftx.com/trade/SHIT-0325', 'https://ftx.com/trade/SHIT-PERP', 
        'https://ftx.com/trade/SKL-PERP', 'https://ftx.com/trade/SLP-PERP', 'https://ftx.com/trade/SNX-PERP', 'https://ftx.com/trade/SOL-0325', 
        'https://ftx.com/trade/SOL-PERP', 'https://ftx.com/trade/SOS-PERP', 'https://ftx.com/trade/SPELL-PERP', 'https://ftx.com/trade/SRM-PERP', 
        'https://ftx.com/trade/SRM/USD', 'https://ftx.com/trade/SRN-PERP', 'https://ftx.com/trade/STEP-PERP', 'https://ftx.com/trade/STMX-PERP', 
        'https://ftx.com/trade/STORJ-PERP', 'https://ftx.com/trade/STX-PERP', 'https://ftx.com/trade/SUSHI-0325', 'https://ftx.com/trade/SUSHI-PERP', 
        'https://ftx.com/trade/SXP-0325', 'https://ftx.com/trade/SXP-PERP', 'https://ftx.com/trade/THETA-0325', 'https://ftx.com/trade/THETA-PERP', 
        'https://ftx.com/trade/TLM-PERP', 'https://ftx.com/trade/TOMO-PERP', 'https://ftx.com/trade/TONCOIN-PERP', 'https://ftx.com/trade/TRU-PERP', 
        'https://ftx.com/trade/TRX-0325', 'https://ftx.com/trade/TRX-PERP', 'https://ftx.com/trade/TRYB-PERP', 'https://ftx.com/trade/TULIP-PERP', 
        'https://ftx.com/trade/UNI-0325', 'https://ftx.com/trade/UNI-PERP', 'https://ftx.com/trade/UNISWAP-0325', 'https://ftx.com/trade/UNISWAP-PERP', 
        'https://ftx.com/trade/USDT-0325', 'https://ftx.com/trade/USDT-PERP', 'https://ftx.com/trade/UST-PERP', 'https://ftx.com/trade/VET-PERP', 
        'https://ftx.com/trade/WAVES-0325', 'https://ftx.com/trade/WAVES-PERP', 'https://ftx.com/trade/XAUT-0325', 'https://ftx.com/trade/XAUT-PERP', 
        'https://ftx.com/trade/XEM-PERP', 'https://ftx.com/trade/XLM-PERP', 'https://ftx.com/trade/XMR-PERP', 'https://ftx.com/trade/XRP-0325', 
        'https://ftx.com/trade/XRP-PERP', 'https://ftx.com/trade/XTZ-0325', 'https://ftx.com/trade/XTZ-PERP', 'https://ftx.com/trade/YFI-0325', 
        'https://ftx.com/trade/YFI-PERP', 'https://ftx.com/trade/YFII-PERP', 'https://ftx.com/trade/ZEC-PERP', 'https://ftx.com/trade/ZIL-PERP', 
        'https://ftx.com/trade/ZRX-PERP', 'https://ftx.com/volume-monitor', 'https://ftx.us/', 'https://help.ftx.com/', 
        'https://help.ftx.com/hc/en-us/articles/360024479432-Fees', 'https://help.ftx.com/hc/en-us/articles/360028737592-How-to-contact-us', 
        'https://help.ftx.com/hc/en-us/sections/4414749476884-Legal', 'https://otc.ftx.com/', 'https://t.me/FTX_Official', 'https://twitter.com/FTX_official']

        actual_find_all_links = self.bot.find_all_links()
        self.assertEqual(expected_original_find_all_links, actual_find_all_links)
        self.assertIsInstance(actual_find_all_links, list)
        for element in actual_find_all_links:
            self.assertIsInstance(element, str)

    def tearDown(self):
        del self.bot

class ScraperValidationTestCase(unittest.TestCase):
    def setUp(self):
        self.bot = scraper2.Scraper('https://ftx.com/markets')
        self.bot.find_all_links()

    def test_valid_links(self):
        expected_original_valid_links = ['https://ftx.com/trade/1INCH-0325', 'https://ftx.com/trade/1INCH-PERP', 'https://ftx.com/trade/AAVE-0325', 
        'https://ftx.com/trade/AAVE-PERP', 'https://ftx.com/trade/ADA-0325', 'https://ftx.com/trade/ADA-PERP', 'https://ftx.com/trade/AGLD-PERP', 
        'https://ftx.com/trade/ALCX-PERP', 'https://ftx.com/trade/ALGO-0325', 'https://ftx.com/trade/ALGO-PERP', 'https://ftx.com/trade/ALICE-PERP', 
        'https://ftx.com/trade/ALPHA-PERP', 'https://ftx.com/trade/ALT-0325', 'https://ftx.com/trade/ALT-PERP', 'https://ftx.com/trade/AMPL-PERP', 
        'https://ftx.com/trade/AR-PERP', 'https://ftx.com/trade/ASD-PERP', 'https://ftx.com/trade/ATLAS-PERP', 'https://ftx.com/trade/ATOM-0325', 
        'https://ftx.com/trade/ATOM-PERP', 'https://ftx.com/trade/AUDIO-PERP', 'https://ftx.com/trade/AVAX-0325', 'https://ftx.com/trade/AVAX-PERP', 
        'https://ftx.com/trade/AXS-PERP', 'https://ftx.com/trade/BADGER-PERP', 'https://ftx.com/trade/BAL-0325', 'https://ftx.com/trade/BAL-PERP', 
        'https://ftx.com/trade/BAND-PERP', 'https://ftx.com/trade/BAO-PERP', 'https://ftx.com/trade/BAT-PERP', 'https://ftx.com/trade/BCH-0325', 
        'https://ftx.com/trade/BCH-PERP', 'https://ftx.com/trade/BIT-PERP', 'https://ftx.com/trade/BNB-0325', 'https://ftx.com/trade/BNB-PERP', 
        'https://ftx.com/trade/BNT-PERP', 'https://ftx.com/trade/BOBA-PERP', 'https://ftx.com/trade/BRZ-PERP', 'https://ftx.com/trade/BSV-0325', 
        'https://ftx.com/trade/BSV-PERP', 'https://ftx.com/trade/BTC-0325', 'https://ftx.com/trade/BTC-0624', 'https://ftx.com/trade/BTC-PERP', 
        'https://ftx.com/trade/BTC-PERP', 'https://ftx.com/trade/BTT-PERP', 'https://ftx.com/trade/C98-PERP', 'https://ftx.com/trade/CAKE-PERP', 
        'https://ftx.com/trade/CEL-0325', 'https://ftx.com/trade/CEL-PERP', 'https://ftx.com/trade/CELO-PERP', 'https://ftx.com/trade/CHR-PERP', 
        'https://ftx.com/trade/CHZ-0325', 'https://ftx.com/trade/CHZ-PERP', 'https://ftx.com/trade/CLV-PERP', 'https://ftx.com/trade/COMP-0325', 
        'https://ftx.com/trade/COMP-PERP', 'https://ftx.com/trade/CONV-PERP', 'https://ftx.com/trade/CREAM-PERP', 'https://ftx.com/trade/CRO-PERP', 
        'https://ftx.com/trade/CRV-PERP', 'https://ftx.com/trade/CUSDT-PERP', 'https://ftx.com/trade/CVC-PERP', 'https://ftx.com/trade/DASH-PERP', 
        'https://ftx.com/trade/DAWN-PERP', 'https://ftx.com/trade/DEFI-0325', 'https://ftx.com/trade/DEFI-PERP', 'https://ftx.com/trade/DENT-PERP', 
        'https://ftx.com/trade/DODO-PERP', 'https://ftx.com/trade/DOGE-0325', 'https://ftx.com/trade/DOGE-PERP', 'https://ftx.com/trade/DOT-0325', 
        'https://ftx.com/trade/DOT-PERP', 'https://ftx.com/trade/DRGN-0325', 'https://ftx.com/trade/DRGN-PERP', 'https://ftx.com/trade/DYDX-PERP', 
        'https://ftx.com/trade/EDEN-0325', 'https://ftx.com/trade/EDEN-PERP', 'https://ftx.com/trade/EGLD-PERP', 'https://ftx.com/trade/ENJ-PERP', 
        'https://ftx.com/trade/ENS-PERP', 'https://ftx.com/trade/EOS-0325', 'https://ftx.com/trade/EOS-PERP', 'https://ftx.com/trade/ETC-PERP', 
        'https://ftx.com/trade/ETH-0325', 'https://ftx.com/trade/ETH-0624', 'https://ftx.com/trade/ETH-PERP', 'https://ftx.com/trade/ETH-PERP', 
        'https://ftx.com/trade/EXCH-0325', 'https://ftx.com/trade/EXCH-PERP', 'https://ftx.com/trade/FIDA-PERP', 'https://ftx.com/trade/FIL-0325', 
        'https://ftx.com/trade/FIL-PERP', 'https://ftx.com/trade/FLM-PERP', 'https://ftx.com/trade/FLOW-PERP', 'https://ftx.com/trade/FTM-PERP', 
        'https://ftx.com/trade/FTT-PERP', 'https://ftx.com/trade/GALA-PERP', 'https://ftx.com/trade/GRT-0325', 'https://ftx.com/trade/GRT-PERP', 
        'https://ftx.com/trade/HBAR-PERP', 'https://ftx.com/trade/HNT-PERP', 'https://ftx.com/trade/HOLY-PERP', 'https://ftx.com/trade/HOT-PERP', 
        'https://ftx.com/trade/HT-PERP', 'https://ftx.com/trade/HUM-PERP', 'https://ftx.com/trade/ICP-PERP', 'https://ftx.com/trade/ICX-PERP', 
        'https://ftx.com/trade/IMX-PERP', 'https://ftx.com/trade/IOTA-PERP', 'https://ftx.com/trade/KAVA-PERP', 'https://ftx.com/trade/KBTT-PERP', 
        'https://ftx.com/trade/KIN-PERP', 'https://ftx.com/trade/KNC-PERP', 'https://ftx.com/trade/KSHIB-PERP', 'https://ftx.com/trade/KSM-PERP', 
        'https://ftx.com/trade/KSOS-PERP', 'https://ftx.com/trade/LEO-PERP', 'https://ftx.com/trade/LINA-PERP', 'https://ftx.com/trade/LINK-0325', 
        'https://ftx.com/trade/LINK-PERP', 'https://ftx.com/trade/LOOKS-PERP', 'https://ftx.com/trade/LRC-PERP', 'https://ftx.com/trade/LTC-0325', 
        'https://ftx.com/trade/LTC-PERP', 'https://ftx.com/trade/LUNA-PERP', 'https://ftx.com/trade/MANA-PERP', 'https://ftx.com/trade/MAPS-PERP', 
        'https://ftx.com/trade/MATIC-PERP', 'https://ftx.com/trade/MCB-PERP', 'https://ftx.com/trade/MEDIA-PERP', 'https://ftx.com/trade/MER-PERP', 
        'https://ftx.com/trade/MID-0325', 'https://ftx.com/trade/MID-PERP', 'https://ftx.com/trade/MINA-PERP', 'https://ftx.com/trade/MKR-PERP', 
        'https://ftx.com/trade/MNGO-PERP', 'https://ftx.com/trade/MTA-PERP', 'https://ftx.com/trade/MTL-PERP', 'https://ftx.com/trade/MVDA10-PERP', 
        'https://ftx.com/trade/MVDA25-PERP', 'https://ftx.com/trade/NEAR-PERP', 'https://ftx.com/trade/NEO-PERP', 'https://ftx.com/trade/OKB-0325', 
        'https://ftx.com/trade/OKB-PERP', 'https://ftx.com/trade/OMG-0325', 'https://ftx.com/trade/OMG-PERP', 'https://ftx.com/trade/ONE-PERP', 
        'https://ftx.com/trade/ONT-PERP', 'https://ftx.com/trade/ORBS-PERP', 'https://ftx.com/trade/OXY-PERP', 'https://ftx.com/trade/PAXG-PERP', 
        'https://ftx.com/trade/PEOPLE-PERP', 'https://ftx.com/trade/PERP-PERP', 'https://ftx.com/trade/POLIS-PERP', 'https://ftx.com/trade/PRIV-0325', 
        'https://ftx.com/trade/PRIV-PERP', 'https://ftx.com/trade/PROM-PERP', 'https://ftx.com/trade/PUNDIX-PERP', 'https://ftx.com/trade/QTUM-PERP', 
        'https://ftx.com/trade/RAMP-PERP', 'https://ftx.com/trade/RAY-PERP', 'https://ftx.com/trade/REEF-0325', 'https://ftx.com/trade/REEF-PERP', 
        'https://ftx.com/trade/REN-PERP', 'https://ftx.com/trade/RNDR-PERP', 'https://ftx.com/trade/RON-PERP', 'https://ftx.com/trade/ROOK-PERP', 
        'https://ftx.com/trade/ROSE-PERP', 'https://ftx.com/trade/RSR-PERP', 'https://ftx.com/trade/RUNE-PERP', 'https://ftx.com/trade/SAND-PERP', 
        'https://ftx.com/trade/SC-PERP', 'https://ftx.com/trade/SCRT-PERP', 'https://ftx.com/trade/SECO-PERP', 'https://ftx.com/trade/SHIB-PERP', 
        'https://ftx.com/trade/SHIT-0325', 'https://ftx.com/trade/SHIT-PERP', 'https://ftx.com/trade/SKL-PERP', 'https://ftx.com/trade/SLP-PERP', 
        'https://ftx.com/trade/SNX-PERP', 'https://ftx.com/trade/SOL-0325', 'https://ftx.com/trade/SOL-PERP', 'https://ftx.com/trade/SOS-PERP', 
        'https://ftx.com/trade/SPELL-PERP', 'https://ftx.com/trade/SRM-PERP', 'https://ftx.com/trade/SRN-PERP', 'https://ftx.com/trade/STEP-PERP', 
        'https://ftx.com/trade/STMX-PERP', 'https://ftx.com/trade/STORJ-PERP', 'https://ftx.com/trade/STX-PERP', 'https://ftx.com/trade/SUSHI-0325', 
        'https://ftx.com/trade/SUSHI-PERP', 'https://ftx.com/trade/SXP-0325', 'https://ftx.com/trade/SXP-PERP', 'https://ftx.com/trade/THETA-0325', 
        'https://ftx.com/trade/THETA-PERP', 'https://ftx.com/trade/TLM-PERP', 'https://ftx.com/trade/TOMO-PERP', 'https://ftx.com/trade/TONCOIN-PERP', 
        'https://ftx.com/trade/TRU-PERP', 'https://ftx.com/trade/TRX-0325', 'https://ftx.com/trade/TRX-PERP', 'https://ftx.com/trade/TRYB-PERP', 
        'https://ftx.com/trade/TULIP-PERP', 'https://ftx.com/trade/UNI-0325', 'https://ftx.com/trade/UNI-PERP', 'https://ftx.com/trade/UNISWAP-0325', 
        'https://ftx.com/trade/UNISWAP-PERP', 'https://ftx.com/trade/USDT-0325', 'https://ftx.com/trade/USDT-PERP', 'https://ftx.com/trade/UST-PERP', 
        'https://ftx.com/trade/VET-PERP', 'https://ftx.com/trade/WAVES-0325', 'https://ftx.com/trade/WAVES-PERP', 'https://ftx.com/trade/XAUT-0325', 
        'https://ftx.com/trade/XAUT-PERP', 'https://ftx.com/trade/XEM-PERP', 'https://ftx.com/trade/XLM-PERP', 'https://ftx.com/trade/XMR-PERP', 
        'https://ftx.com/trade/XRP-0325', 'https://ftx.com/trade/XRP-PERP', 'https://ftx.com/trade/XTZ-0325', 'https://ftx.com/trade/XTZ-PERP', 
        'https://ftx.com/trade/YFI-0325', 'https://ftx.com/trade/YFI-PERP', 'https://ftx.com/trade/YFII-PERP', 'https://ftx.com/trade/ZEC-PERP', 
        'https://ftx.com/trade/ZIL-PERP', 'https://ftx.com/trade/ZRX-PERP']

        actual_valid_links = self.bot.valid_links()
        self.assertEqual(expected_original_valid_links, actual_valid_links)
        self.assertIsInstance(actual_valid_links, list)
        for element in actual_valid_links:
            self.assertEqual(element[0:22], 'https://ftx.com/trade/') 
            self.assertIsInstance(element, str)

    def tearDown(self):
        del self.bot

class ScraperDataTestCase(unittest.TestCase):
    def setUp(self):
        self.bot = scraper2.Scraper('https://ftx.com/markets')
        self.bot.find_all_links()
        self.bot.valid_links()
        

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)