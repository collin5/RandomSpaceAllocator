#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: tests/test_print_allocations.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 28.06.2017
# Last Modified: 28.06.2017

from unittest import TestCase
from modules.amity import Amity


class PrintAllocationsTestCase(TestCase):

    def setUp(self):
        self.amity = Amity

    def print_allocations_successfully(self):
        self.amity.create_room('office', 'ruby')
        self.amity.add_person('Edwin', 'Kato', 'fellow')
        stdout = self.amity.print_allocations()
        self.assertTrue('Edwin' in stdout)

    def print_allocations_successfully_2(self):
        self.amity.create_room('office', 'shell')
        self.amity.add_person('Dona', 'Mwine', 'fellow')
        self.amity.add_person('Shem', 'O', 'staff')
        stdout = self.amity.print_allocations()
        self.assertTrue('Dona' in stdout)
        self.assertTrue('Shem' in stdout)

    def print_allocations_with_living_room(self):
        self.amity.create_room('office', 'oculus')
        self.amity.create_room('living', 'catherines')
        self.amity.add_person('collins', 'a', 'fellow', True)

        stdout = self.amity.print_allocations()
        self.assertTrue('catherines' in stdout)
        self.assertTrue('collins' in stdout)
