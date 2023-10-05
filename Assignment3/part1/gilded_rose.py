# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def get_item_sell_in(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item.sell_in
        return None

    def get_item_quality(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item.quality
        return None

    def conjured_item(self, item):
        if item.sell_in > 0:
            degrade = 2
        else:
            degrade = 4

        if (item.quality - degrade) > 0:
            item.quality = item.quality - degrade
        else:
            item.quality = 0

        item.sell_in -= 1

    def normal_item(self, item):
        if item.sell_in > 0:
            degrade = 1
        else:
            degrade = 2

        if (item.quality - degrade) > 0:
            item.quality = item.quality - degrade
        else:
            item.quality = 0

        item.sell_in -= 1

    def aged_brie(self, item):
        if item.sell_in > 0:
            degrade = -1
        else:
            degrade = -2

        if (item.quality - degrade) < 50:
            item.quality = item.quality - degrade
        else:
            item.quality = 50
    
        item.sell_in -= 1

    def backstage_passes(self, item):
        if item.sell_in > 10 and item.sell_in < 50:
            degrade = -1
            item.quality = item.quality - degrade
        elif item.sell_in > 5 and item.sell_in < 10:
            degrade = -2
            item.quality = item.quality - degrade
        elif item.sell_in < 5 and item.sell_in > 0:
            degrade = -3
            item.quality = item.quality - degrade
        else:
            item.quality = 50

        item.sell_in -= 1

    def sulfuras(self, item):
        pass


    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.sulfuras(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.backstage_passes(item)
            elif item.name == ("Conjured Mana Cake"):
                self.conjured_item(item)
            else:
                self.normal_item(item)
