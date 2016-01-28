#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit tests for rinse.util module."""

import unittest
from lxml import etree

from ..util import recursive_dict


class TestRecursiveDict(unittest.TestCase):
    def test_recursive_dict_function(self):
        doc = etree.fromstring('''<?xml version="1.0" encoding="UTF-8"?>
            <SOAP-ENV:Envelope
              xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
              xmlns:ns1="https://example.com/soap/v3"
              xmlns:xsd="http://www.w3.org/2001/XMLSchema"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
              SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
              <SOAP-ENV:Body>
                <ns1:authenticateResponse>
                  <return xsi:type="ns1:ApiAuthenticateResult">
                    <token xsi:type="xsd:string">1234567890</token>
                    <error xsi:type="ns1:ApiError">
                      <number xsi:type="xsd:int">0</number>
                      <description xsi:type="xsd:string">No Error</description>
                    </error>
                  </return>
                </ns1:authenticateResponse>
              </SOAP-ENV:Body>
            </SOAP-ENV:Envelope>
        ''')

        recursive_dict(doc)
