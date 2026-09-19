class GildedRose(object):

    MAX_QUALITY = 50

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_item(item)

    def _update_item(self, item):
        match item.name:
            case "Sulfuras, Hand of Ragnaros":
                return
            case "Aged Brie":
                self._update_aged_brie(item)
            case "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_pass(item)
            case _ if item.name.startswith("Conjured "):
                self._update_conjured(item)
            case _:
                self._update_normal(item)

    def _update_normal(self, item):
        if item.sell_in <= 0:
            decrease = 2
        else:
            decrease = 1

        self._change_quality(item, -decrease)
        item.sell_in -= 1

    def _update_aged_brie(self, item):
        if item.sell_in <= 0:
            increase = 2
        else:
            increase = 1

        self._change_quality(item, increase)
        item.sell_in -= 1

    def _update_backstage_pass(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        else:
            increase = 1

            if item.sell_in <= 10:
                increase += 1

            if item.sell_in <= 5:
                increase += 1

            self._change_quality(item, increase)

        item.sell_in -= 1

    def _update_conjured(self, item):
        if item.sell_in <= 0:
            decrease = 4
        else:
            decrease = 2

        self._change_quality(item, -decrease)
        item.sell_in -= 1

    def _change_quality(self, item, amount):
        new_quality = item.quality + amount

        if new_quality < 0:
            new_quality = 0
        elif new_quality > self.MAX_QUALITY:
            new_quality = self.MAX_QUALITY

        item.quality = new_quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
