# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    #def test_foo(self):
        #items = [Item("foo", 0, 0)]
        #gilded_rose = GildedRose(items)
        #gilded_rose.update_quality()
        #self.assertEquals("fixme", items[0].name)

    def test_conjured_item(self):
        # Arrange
        items = [Item("Conjured Mana Cake", 5, 42)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Conjured Mana Cake")
        original_quality = gr.get_item_quality("Conjured Mana Cake")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Conjured Mana Cake")
        new_quality = gr.get_item_quality("Conjured Mana Cake")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality < original_quality
        assert new_quality == original_quality - 2


    def test_normal_item(self):
        # Arrange
        items = [Item("Normal", 4, 10)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Normal")
        original_quality = gr.get_item_quality("Normal")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Normal")
        new_quality = gr.get_item_quality("Normal")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality < original_quality
        assert new_quality == original_quality - 1


    def test_aged_brie(self):
        # Arrange
        items = [Item("Aged Brie", 5, 10)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Aged Brie")
        original_quality = gr.get_item_quality("Aged Brie")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Aged Brie")
        new_quality = gr.get_item_quality("Aged Brie")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality > original_quality
        assert new_quality == original_quality + 1


    def test_backstage_pass(self):
        # Arrange
        items = [Item("Backstage Passes", 10, 10)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Backstage Passes")
        original_quality = gr.get_item_quality("Backstage Passes")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Backstage Passes")
        new_quality = gr.get_item_quality("Backstage Passes")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50











if __name__ == '__main__':
    unittest.main()
