#! /usr/bin/env python
#
# Copyright © 2009, Lorenzo Pallara l.pallara@avlapa.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import string
from dvbobjects.MPEG.EBUTeletext import *
from dvbobjects.utils import *

# where to insert the signalling in the analog video
#                field_parity = 1        field_parity = 0
# 0x00		     Line number undefined   Line number undefined
# 0x01 to 0x06   reserved for future use reserved for future use
# 0x07           Line number = 7         Line number = 320
# 0x08           Line number = 8         Line number = 321
#  :                    :                       :
# 0x16           Line number = 22        Line number = 335
# 0x17 to 0x1F	reserved for future use		reserved for future use

#       C4        Byte 9, bit 8 Packets X/1 to X/28 belonging to a previous transmission of the page should
#  Erase Page                   be erased from the decoder's memory before packets belonging to the
#                               associated page are stored.
#       C5        Byte 11, bit When set to '1' this bit indicates that the associated page is a Newsflash
#  Newsflash          6        page. All information intended for display on such a page will be boxed and
#                               will be displayed inset into the normal video picture.
#       C6        Byte 11, bit When set to '1' this bit indicates that the associated page is a subtitle page.
#     Subtitle         8        All information intended for display on such a page will be boxed and will be
#                               displayed inset into the normal video picture.
#       C7        Byte 12, bit Data addressed to row 0 is not to be displayed.
#    Suppress          2
#     Header
#       C8        Byte 12, bit Data within packets X/1 to X/28 of the associated page has been changed
#     Update           4        since the previous transmission. The setting of this bit is under editorial
#    Indicator                  control.
#       C9        Byte 12, bit The associated page is not in numerical order of page sequence, allowing
#  Interrupted        6        the header to be excluded from a rolling header display to avoid
#    Sequence                   discontinuities.
#       C10       Byte 12, bit Data addressed to rows 1 to 24 is not to be displayed.
# Inhibit Display      8
#       C11       Byte 13, bit When set to '1' the service is designated to be in Serial mode and the
# Magazine Serial       2        transmission of a page is terminated by the next page header with a different
#                               page number.
#                               When set to '0' the service is designated to be in Parallel mode and the
#                               transmission of a page is terminated by the next page header with a different
#                               page number but the same magazine number.
#                               The same setting shall be used for all page headers in the service.
# C12, C13, C14       Byte       Where the decoder is capable of displaying text in more than one language
# National Option 13, bits 4, 6  these control bits are used to select G0 character set options, (see
#    Character       and 8      subclause 15.2). The response to these control bits may be modified by
#     Subset                    packets X/28/0 Format 1, X/28/4, M/29/0 and M/29/4.


# country codes
# 000  English  or  Polish
# 001  German
# 010  Swedish
# 011  Italian
# 100  French
# 101  Spanish  or  Serbo-croat
# 110  Turkish  or  Czechoslovakia
# 111  Rumanian


teletextunitspage1 = EBUTeletextUnits(
    unit_loop = [
        EBUTeletext(
            data_unit_id = 0x02,  # 0x02 non-subtitle, 0x03 subtitles, 0xFF stuffing
            field_parity = 0o1,
            line_offset = 0x7,
            magazine = 0x01,
            row = 0x00,  # 24 (0x17) lines per magazine, 0 is the page header
            page = 0x00,
            subpage = 0x0000,
            erase_page = 0,
            newsflash = 0,
            subtitle = 0,
            suppress_header = 0,
            update_indicator = 1,
            interrupted_sequence = 0,
            inhibit_display = 0,
            magazine_serial = 1,
            country_code = 0x03,
            chars = b"    Avalpa-TXT  10 04 2009 15 00"
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x8,
            magazine = 0x01,
            row = 0x01,
            chars = b" Avalpa1            " +
            b" Avalpa1            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x9,
            magazine = 0x01,
            row = 0x02,
            chars = b" Avalpa2            " +
            b" Avalpa2            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xA,
            magazine = 0x01,
            row = 0x03,
            chars = b" Avalpa3            " +
            b" Avalpa3            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xB,
            magazine = 0x01,
            row = 0x04,
            chars = b" Avalpa4            " +
            b" Avalpa4            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xC,
            magazine = 0x01,
            row = 0x05,
            chars = b" Avalpa5            " +
            b" Avalpa5            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xD,
            magazine = 0x01,
            row = 0x06,
            chars = b" Avalpa6            " +
            b" Avalpa6            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xE,
            magazine = 0x01,
            row = 0x07,
            chars = b" Avalpa7            " +
            b" Avalpa7            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xF,
            magazine = 0x01,
            row = 0x08,
            chars = b" Avalpa8            " +
            b" Avalpa8            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x10,
            magazine = 0x01,
            row = 0x09,
            chars = b" Avalpa9            " +
            b" Avalpa9            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x13,
            magazine = 0x01,
            row = 0x0A,
            chars = b" Avalpa10           " +
            b" Avalpa10           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x14,
            magazine = 0x01,
            row = 0x0B,
            chars = b" Avalpa11           " +
            b" Avalpa11           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x15,
            magazine = 0x01,
            row = 0x0C,
            chars = b" Avalpa12           " +
            b" Avalpa12           ",
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),

        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x8,
            magazine = 0x01,
            row = 0x0D,
            chars = b" avalpa1            " +
            b" avalpa1            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x9,
            magazine = 0x01,
            row = 0x0E,
            chars = b" avalpa2            " +
            b" avalpa2            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xA,
            magazine = 0x01,
            row = 0x0F,
            chars = b" avalpa3            " +
            b" avalpa3            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xB,
            magazine = 0x01,
            row = 0x10,
            chars = b" avalpa4            " +
            b" avalpa4            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xC,
            magazine = 0x01,
            row = 0x11,
            chars = b" avalpa5            " +
            b" avalpa5            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xD,
            magazine = 0x01,
            row = 0x12,
            chars = b" avalpa6            " +
            b" avalpa6            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xE,
            magazine = 0x01,
            row = 0x13,
            chars = b" avalpa7            " +
            b" avalpa7            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xF,
            magazine = 0x01,
            row = 0x14,
            chars = b" avalpa8            " +
            b" avalpa8            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x10,
            magazine = 0x01,
            row = 0x15,
            chars = b" avalpa9            " +
            b" avalpa9            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x13,
            magazine = 0x01,
            row = 0x16,
            chars = b" avalpa10           " +
            b" avalpa10           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x14,
            magazine = 0x01,
            row = 0x17,
            chars = b" avalpa11           " +
            b" avalpa11           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x15,
            magazine = 0x01,
            row = 27,  # special packet
            designation_code = 0,  # version 0
            link1 = EBUTeletextLink(
                magazine = 0x2,
                page = 0x02,
                subpage = 0x0000,
            ),
            link2 = EBUTeletextLink(
                magazine = 0x2,
                page = 0x22,
                subpage = 0x0000,
            ),
            link3 = EBUTeletextLink(
                magazine = 0x2,
                page = 0x02,
                subpage = 0x0000,
            ),
            link4 = EBUTeletextLink(
                magazine = 0x4,
                page = 0x04,
                subpage = 0x0000,
            ),
            link5 = EBUTeletextLink(
                magazine = 0x4,
                page = 0x04,
                subpage = 0x0000,
            ),
            link6 = EBUTeletextLink(
                magazine = 0x4,
                page = 0x04,
                subpage = 0x0000,
            ),
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
    ]
)

teletextunitspage2 = EBUTeletextUnits(
    unit_loop = [
        EBUTeletext(
            data_unit_id = 0x02,  # 0x02 non-subtitle, 0x03 subtitles, 0xFF stuffing
            field_parity = 0o1,
            line_offset = 0x7,
            magazine = 0x02,
            row = 0x00,  # 24 (0x17) lines per magazine, 0 is the page header
            page = 0x02,
            subpage = 0x0000,
            erase_page = 0,
            newsflash = 0,
            subtitle = 0,
            suppress_header = 0,
            update_indicator = 1,
            interrupted_sequence = 0,
            inhibit_display = 0,
            magazine_serial = 1,
            country_code = 0x03,
            chars = b"    Avalpa-TXT  10 04 2009 15 00"
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x8,
            magazine = 0x02,
            row = 0x01,
            chars = b" A_202_1            " +
            b" A_202_1            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x9,
            magazine = 0x02,
            row = 0x02,
            chars = b" A_202_2            " +
            b" A_202_2            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xA,
            magazine = 0x02,
            row = 0x03,
            chars = b" A_202_3            " +
            b" A_202_3            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xB,
            magazine = 0x02,
            row = 0x04,
            chars = b" A_202_4            " +
            b" A_202_4            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xC,
            magazine = 0x02,
            row = 0x05,
            chars = b" A_202_5            " +
            b" A_202_5            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xD,
            magazine = 0x02,
            row = 0x06,
            chars = b" A_202_6            " +
            b" A_202_6            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xE,
            magazine = 0x02,
            row = 0x07,
            chars = b" A_202_7            " +
            b" A_202_7            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xF,
            magazine = 0x02,
            row = 0x08,
            chars = b" A_202_8            " +
            b" A_202_8            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x10,
            magazine = 0x02,
            row = 0x09,
            chars = b" A_202_9            " +
            b" A_202_9            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x13,
            magazine = 0x02,
            row = 0x0A,
            chars = b" A_202_10           " +
            b" A_202_10           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x14,
            magazine = 0x02,
            row = 0x0B,
            chars = b" A_202_11           " +
            b" A_202_11           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x15,
            magazine = 0x02,
            row = 0x0C,
            chars = b" A_202_12           " +
            b" A_202_12           ",
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),

        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x8,
            magazine = 0x02,
            row = 0x0D,
            chars = b" a_202_1            " +
            b" a_202_1            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x9,
            magazine = 0x02,
            row = 0x0E,
            chars = b" a_202_2            " +
            b" a_202_2            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xA,
            magazine = 0x02,
            row = 0x0F,
            chars = b" a_202_3            " +
            b" a_202_3            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xB,
            magazine = 0x02,
            row = 0x10,
            chars = b" a_202_4            " +
            b" a_202_4            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xC,
            magazine = 0x02,
            row = 0x11,
            chars = b" a_202_5            " +
            b" a_202_5            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xD,
            magazine = 0x02,
            row = 0x12,
            chars = b" a_202_6            " +
            b" a_202_6            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xE,
            magazine = 0x02,
            row = 0x13,
            chars = b" a_202_7            " +
            b" a_202_7            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xF,
            magazine = 0x02,
            row = 0x14,
            chars = b" a_202_8            " +
            b" a_202_8            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x10,
            magazine = 0x02,
            row = 0x15,
            chars = b" a_202_9            " +
            b" a_202_9            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x13,
            magazine = 0x02,
            row = 0x16,
            chars = b" a_202_10           " +
            b" a_202_10           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x14,
            magazine = 0x02,
            row = 0x17,
            chars = b" a_202_11           " +
            b" a_202_11           ",
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
    ]
)

teletextunitspage3 = EBUTeletextUnits(
    unit_loop = [
        EBUTeletext(
            data_unit_id = 0x02,  # 0x02 non-subtitle, 0x03 subtitles, 0xFF stuffing
            field_parity = 0o1,
            line_offset = 0x7,
            magazine = 0x03,
            row = 0x00,  # 24 (0x17) lines per magazine, 0 is the page header
            page = 0x02,
            subpage = 0x0000,
            erase_page = 0,
            newsflash = 0,
            subtitle = 0,
            suppress_header = 0,
            update_indicator = 1,
            interrupted_sequence = 0,
            inhibit_display = 0,
            magazine_serial = 1,
            country_code = 0x03,
            chars = b"    Avalpa-TXT  10 04 2009 15 00"
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x8,
            magazine = 0x03,
            row = 0x01,
            chars = b" A_302_1            " +
            b" A_302_1            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x9,
            magazine = 0x03,
            row = 0x02,
            chars = b" A_302_2            " +
            b" A_302_2            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xA,
            magazine = 0x03,
            row = 0x03,
            chars = b" A_302_3            " +
            b" A_302_3            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xB,
            magazine = 0x03,
            row = 0x04,
            chars = b" A_302_4            " +
            b" A_302_4            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xC,
            magazine = 0x03,
            row = 0x05,
            chars = b" A_302_5            " +
            b" A_302_5            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xD,
            magazine = 0x03,
            row = 0x06,
            chars = b" A_302_6            " +
            b" A_302_6            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xE,
            magazine = 0x03,
            row = 0x07,
            chars = b" A_302_7            " +
            b" A_302_7            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xF,
            magazine = 0x03,
            row = 0x08,
            chars = b" A_302_8            " +
            b" A_302_8            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x10,
            magazine = 0x03,
            row = 0x09,
            chars = b" A_302_9            " +
            b" A_302_9            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x13,
            magazine = 0x03,
            row = 0x0A,
            chars = b" A_302_10           " +
            b" A_302_10           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x14,
            magazine = 0x03,
            row = 0x0B,
            chars = b" A_302_11           " +
            b" A_302_11           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x15,
            magazine = 0x03,
            row = 0x0C,
            chars = b" A_302_12           " +
            b" A_302_12           ",
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),

        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x8,
            magazine = 0x03,
            row = 0x0D,
            chars = b" a_302_1            " +
            b" a_302_1            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x9,
            magazine = 0x03,
            row = 0x0E,
            chars = b" a_302_2            " +
            b" a_302_2            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xA,
            magazine = 0x03,
            row = 0x0F,
            chars = b" a_302_3            " +
            b" a_302_3            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xB,
            magazine = 0x03,
            row = 0x10,
            chars = b" a_302_4            " +
            b" a_302_4            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xC,
            magazine = 0x03,
            row = 0x11,
            chars = b" a_302_5            " +
            b" a_302_5            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xD,
            magazine = 0x03,
            row = 0x12,
            chars = b" a_302_6            " +
            b" a_302_6            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xE,
            magazine = 0x03,
            row = 0x13,
            chars = b" a_302_7            " +
            b" a_302_7            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xF,
            magazine = 0x03,
            row = 0x14,
            chars = b" a_302_8            " +
            b" a_302_8            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x10,
            magazine = 0x03,
            row = 0x15,
            chars = b" a_302_9            " +
            b" a_302_9            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x13,
            magazine = 0x03,
            row = 0x16,
            chars = b" a_302_10           " +
            b" a_302_10           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x14,
            magazine = 0x03,
            row = 0x17,
            chars = b" a_302_11           " +
            b" a_302_11           ",
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),


    ]
)


teletextunitspage4 = EBUTeletextUnits(
    unit_loop = [
        EBUTeletext(
            data_unit_id = 0x02,  # 0x02 non-subtitle, 0x03 subtitles, 0xFF stuffing
            field_parity = 0o1,
            line_offset = 0x7,
            magazine = 0x04,
            row = 0x00,  # 24 (0x17) lines per magazine, 0 is the page header
            page = 0x04,
            subpage = 0x0000,
            erase_page = 0,
            newsflash = 0,
            subtitle = 0,
            suppress_header = 0,
            update_indicator = 1,
            interrupted_sequence = 0,
            inhibit_display = 0,
            magazine_serial = 1,
            country_code = 0x03,
            chars = b"    Avalpa-TXT  10 04 2009 15 00"
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x8,
            magazine = 0x04,
            row = 0x01,
            chars = b" A_404_1            " +
            b" A_404_1            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x9,
            magazine = 0x04,
            row = 0x02,
            chars = b" A_404_2            " +
            b" A_404_2            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xA,
            magazine = 0x04,
            row = 0x03,
            chars = b" A_404_3            " +
            b" A_404_3            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xB,
            magazine = 0x04,
            row = 0x04,
            chars = b" A_404_4            " +
            b" A_404_4            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xC,
            magazine = 0x04,
            row = 0x05,
            chars = b" A_404_5            " +
            b" A_404_5            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xD,
            magazine = 0x04,
            row = 0x06,
            chars = b" A_404_6            " +
            b" A_404_6            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xE,
            magazine = 0x04,
            row = 0x07,
            chars = b" A_404_7            " +
            b" A_404_7            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0xF,
            magazine = 0x04,
            row = 0x08,
            chars = b" A_404_8            " +
            b" A_404_8            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x10,
            magazine = 0x04,
            row = 0x09,
            chars = b" A_404_9            " +
            b" A_404_9            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x13,
            magazine = 0x04,
            row = 0x0A,
            chars = b" A_404_10           " +
            b" A_404_10           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x14,
            magazine = 0x04,
            row = 0x0B,
            chars = b" A_404_11           " +
            b" A_404_11           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 0o1,
            line_offset = 0x15,
            magazine = 0x04,
            row = 0x0C,
            chars = b" A_404_12           " +
            b" A_404_12           ",
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),

        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x8,
            magazine = 0x04,
            row = 0x0D,
            chars = b" a_404_1            " +
            b" a_404_1            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x9,
            magazine = 0x04,
            row = 0x0E,
            chars = b" a_404_2            " +
            b" a_404_2            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xA,
            magazine = 0x04,
            row = 0x0F,
            chars = b" a_404_3            " +
            b" a_404_3            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xB,
            magazine = 0x04,
            row = 0x10,
            chars = b" a_404_4            " +
            b" a_404_4            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xC,
            magazine = 0x04,
            row = 0x11,
            chars = b" a_404_5            " +
            b" a_404_5            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xD,
            magazine = 0x04,
            row = 0x12,
            chars = b" a_404_6            " +
            b" a_404_6            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xE,
            magazine = 0x04,
            row = 0x13,
            chars = b" a_404_7            " +
            b" a_404_7            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0xF,
            magazine = 0x04,
            row = 0x14,
            chars = b" a_404_8            " +
            b" a_404_8            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x10,
            magazine = 0x04,
            row = 0x15,
            chars = b" a_404_9            " +
            b" a_404_9            ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x13,
            magazine = 0x04,
            row = 0x16,
            chars = b" a_404_10           " +
            b" a_404_10           ",
        ),
        EBUTeletext(
            data_unit_id = 0x02,
            field_parity = 00,
            line_offset = 0x14,
            magazine = 0x04,
            row = 0x17,
            chars = b" a_404_11           " +
            b" a_404_11           ",
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),
        EBUTeletext(
            data_unit_id = 0xFF,
        ),


    ]
)


out = open("./page1.txt", "wb")
out.write(teletextunitspage1.pack())
out.close()

out = open("./page2.txt", "wb")
out.write(teletextunitspage2.pack())
out.close()

out = open("./page3.txt", "wb")
out.write(teletextunitspage3.pack())
out.close()

out = open("./page4.txt", "wb")
out.write(teletextunitspage4.pack())
out.close()
