# -*- coding: UTF-8 -*-
# Copyright (C) 2009 Itaapy, ArsAperta, Pierlis, Talend

# Import from the Standard Library
from unittest import TestCase, main

# Import from itools
from itools.xml import XML_DECL, START_ELEMENT

# Import from lpod
from lpod.container import get_odf_container
from lpod.context import create_element
from lpod.context import odf_element, odf_context


class CreateElementTestCase(TestCase):

    def test_simple(self):
        element = create_element('<office:document></office:document>')



class ElementTestCase(TestCase):

    def setUp(self):
        container = get_odf_container('samples/example.odt')
        self.container = container
        content_context = odf_context('content', container)
        self.content_context = content_context
        paragraph_element = content_context.get_element_list('//text:p[1]')
        self.paragraph_element = paragraph_element[0]


    def tearDown(self):
        del self.paragraph_element
        del self.content_context
        del self.container


    def test_get_element_list(self):
        raise NotImplementedError


    def test_get_attribute(self):
        element = self.paragraph_element
        self.assertEqual(element.get_attribute('text:style-name'),
                         'Standard')


    def test_set_attribute(self):
        raise NotImplementedError


    def test_get_text(self):
        element = self.paragraph_element
        self.assertEqual(element.get_text(), u"This is an example.")


    def test_set_text(self):
        raise NotImplementedError


    def test_insert_element(self):
        raise NotImplementedError


    def test_copy(self):
        raise NotImplementedError


    def test_delete(self):
        raise NotImplementedError



class ContextTestCase(TestCase):

    def setUp(self):
        self.container = get_odf_container('samples/example.odt')


    def tearDown(self):
        del self.container


    def test_get_element_list(self):
        raise NotImplementedError


    def serialize(self):
        container = self.container
        content_bytes = container.get_part('content')
        context = odf_context('content', container)
        self.assertEqual(content_bytes, context.serialize())



if __name__ == '__main__':
    main()