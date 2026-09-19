import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def item_change(self, name, sell_in, quality):
        item = Item(name, sell_in, quality)
        GildedRose([item]).update_quality()
        return item

    # Normal Items
    def test_normal_item_before_expiry(self):
        item = self.item_change("Elixir of the Mongoose", 7, 15)

        self.assertEqual(6, item.sell_in)
        self.assertEqual(14, item.quality)

    def test_normal_item_at_expiry(self):
        item = self.item_change("Elixir of the Mongoose", 0, 25)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(23, item.quality)

    def test_normal_item_already_expired(self):
        item = self.item_change("Elixir of the Mongoose", -3, 18)

        self.assertEqual(-4, item.sell_in)
        self.assertEqual(16, item.quality)

    def test_normal_item_quality_at_zero(self):
        item = self.item_change("Elixir of the Mongoose", 6, 0)

        self.assertEqual(5, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_normal_item_quality_one_at_expiry(self):
        item = self.item_change("Elixir of the Mongoose", 0, 1)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

    # Aged Brie
    def test_aged_brie_before_expiry(self):
        item = self.item_change("Aged Brie", 8, 20)

        self.assertEqual(7, item.sell_in)
        self.assertEqual(21, item.quality)

    def test_aged_brie_at_expiry(self):
        item = self.item_change("Aged Brie", 0, 20)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(22, item.quality)

    def test_aged_brie_quality_49(self):
        item = self.item_change("Aged Brie", 5, 49)

        self.assertEqual(4, item.sell_in)
        self.assertEqual(50, item.quality)

    def test_aged_brie_quality_50(self):
        item = self.item_change("Aged Brie", 4, 50)

        self.assertEqual(3, item.sell_in)
        self.assertEqual(50, item.quality)

    def test_aged_brie_expired_quality_49(self):
        item = self.item_change("Aged Brie", 0, 49)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(50, item.quality)

    # Sulfuras
    def test_sulfuras_before_expiry(self):
        item = self.item_change(
            "Sulfuras, Hand of Ragnaros",
            8,
            80
        )

        self.assertEqual(8, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_sulfuras_at_expiry(self):
        item = self.item_change(
            "Sulfuras, Hand of Ragnaros",
            0,
            80
        )

        self.assertEqual(0, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_sulfuras_already_expired(self):
        item = self.item_change(
            "Sulfuras, Hand of Ragnaros",
            -4,
            80
        )

        self.assertEqual(-4, item.sell_in)
        self.assertEqual(80, item.quality)


    # Backstage Passes
    def test_backstage_pass_before_10_days(self):
        item = self.item_change(
            "Backstage passes to a TAFKAL80ETC concert",
            14,
            20
        )

        self.assertEqual(13, item.sell_in)
        self.assertEqual(21, item.quality)

    def test_backstage_pass_at_11_days(self):
        item = self.item_change(
            "Backstage passes to a TAFKAL80ETC concert",
            11,
            20
        )

        self.assertEqual(10, item.sell_in)
        self.assertEqual(21, item.quality)

    def test_backstage_pass_at_10_days(self):
        item = self.item_change(
            "Backstage passes to a TAFKAL80ETC concert",
            10,
            20
        )

        self.assertEqual(9, item.sell_in)
        self.assertEqual(22, item.quality)

    def test_backstage_pass_at_6_days(self):
        item = self.item_change(
            "Backstage passes to a TAFKAL80ETC concert",
            6,
            20
        )

        self.assertEqual(5, item.sell_in)
        self.assertEqual(22, item.quality)

    def test_backstage_pass_at_5_days(self):
        item = self.item_change(
            "Backstage passes to a TAFKAL80ETC concert",
            5,
            20
        )

        self.assertEqual(4, item.sell_in)
        self.assertEqual(23, item.quality)

    def test_backstage_pass_at_1_day(self):
        item = self.item_change(
            "Backstage passes to a TAFKAL80ETC concert",
            1,
            30
        )

        self.assertEqual(0, item.sell_in)
        self.assertEqual(33, item.quality)

    def test_backstage_pass_at_expiry(self):
        item = self.item_change(
            "Backstage passes to a TAFKAL80ETC concert",
            0,
            30
        )

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_backstage_pass_already_expired(self):
        item = self.item_change(
            "Backstage passes to a TAFKAL80ETC concert",
            -2,
            35
        )

        self.assertEqual(-3, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_backstage_pass_quality_49(self):
        item = self.item_change(
            "Backstage passes to a TAFKAL80ETC concert",
            7,
            49
        )

        self.assertEqual(6, item.sell_in)
        self.assertEqual(50, item.quality)

    def test_backstage_pass_quality_50(self):
        item = self.item_change(
            "Backstage passes to a TAFKAL80ETC concert",
            3,
            50
        )

        self.assertEqual(2, item.sell_in)
        self.assertEqual(50, item.quality)

    
    # Conjured Items
    def test_conjured_item_before_expiry(self):
        item = self.item_change("Conjured Mana Cake", 9, 20)

        self.assertEqual(8, item.sell_in)
        self.assertEqual(18, item.quality)

    def test_conjured_item_at_expiry(self):
        item = self.item_change("Conjured Mana Cake", 0, 20)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(16, item.quality)

    def test_conjured_item_already_expired(self):
        item = self.item_change("Conjured Mana Cake", -2, 20)

        self.assertEqual(-3, item.sell_in)
        self.assertEqual(16, item.quality)

    def test_conjured_item_quality_one(self):
        item = self.item_change("Conjured Mana Cake", 6, 1)

        self.assertEqual(5, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_conjured_item_quality_zero(self):
        item = self.item_change("Conjured Mana Cake", 6, 0)

        self.assertEqual(5, item.sell_in)
        self.assertEqual(0, item.quality)

        
    # Boundary Cases

    def test_normal_item_quality_one_before_expiry(self):
        item = self.item_change("Elixir of the Mongoose", 5, 1)

        self.assertEqual(4, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_normal_item_quality_zero_after_expiry(self):
        item = self.item_change("Elixir of the Mongoose", -2, 0)

        self.assertEqual(-3, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_aged_brie_quality_zero_after_expiry(self):
        item = self.item_change("Aged Brie", -1, 0)

        self.assertEqual(-2, item.sell_in)
        self.assertEqual(2, item.quality)

    def test_aged_brie_quality_50_after_expiry(self):
        item = self.item_change("Aged Brie", -1, 50)

        self.assertEqual(-2, item.sell_in)
        self.assertEqual(50, item.quality)

    def test_backstage_pass_quality_48_at_5_days(self):
        item = self.item_change(
            "Backstage passes to a TAFKAL80ETC concert",
            5,
            48
        )

        self.assertEqual(4, item.sell_in)
        self.assertEqual(50, item.quality)

    def test_backstage_pass_quality_49_at_1_day(self):
        item = self.item_change(
            "Backstage passes to a TAFKAL80ETC concert",
            1,
            49
        )

        self.assertEqual(0, item.sell_in)
        self.assertEqual(50, item.quality)

    def test_conjured_item_quality_three_before_expiry(self):
        item = self.item_change("Conjured Mana Cake", 5, 3)

        self.assertEqual(4, item.sell_in)
        self.assertEqual(1, item.quality)

    def test_conjured_item_quality_three_after_expiry(self):
        item = self.item_change("Conjured Mana Cake", -1, 3)

        self.assertEqual(-2, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_conjured_item_quality_50_before_expiry(self):
        item = self.item_change("Conjured Mana Cake", 5, 50)

        self.assertEqual(4, item.sell_in)
        self.assertEqual(48, item.quality)


if __name__ == '__main__':
    unittest.main()
