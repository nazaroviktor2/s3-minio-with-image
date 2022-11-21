from unittest import TestCase, main

from exceptions import InvalidImageFormat
from random_image import get_images_json, save_image


class ImageTest(TestCase):
    def test_get_images_json_len(self):
        self.assertEqual(len(get_images_json(100)), 100)
        self.assertEqual(len(get_images_json(0)), 0)

    def test_get_images_json_type(self):
        self.assertEqual(type(get_images_json(1)), list)

    def test_get_images_json_have_uid(self):
        images = get_images_json(1)
        self.assertTrue("url" in images[0].keys())

    def test_get_images_json_have_image(self):
        images = get_images_json(1)
        self.assertTrue("image" in images[0].keys())

    def test_save_image_exception_InvalidImageFormat(self):
        self.assertRaises(InvalidImageFormat, save_image, {"not uid": "some",
                                                           "not image": "some"})


if __name__ == '__main__':
    main()
