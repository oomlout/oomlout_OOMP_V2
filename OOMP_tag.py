import OOMP
import src.tag.OOMP_tag_NAMES

import src.tag.OOMP_tag_DETAILS_type
import src.tag.OOMP_tag_DETAILS_size
import src.tag.OOMP_tag_DETAILS_color
import src.tag.OOMP_tag_DETAILS_desc
import src.tag.OOMP_tag_DETAILS_index

OOMP.load()
src.tag.OOMP_tag_NAMES.load(OOMP.tagNames)
src.tag.OOMP_tag_DETAILS_type.load(OOMP.tagDetails)
src.tag.OOMP_tag_DETAILS_size.load(OOMP.tagDetails)
src.tag.OOMP_tag_DETAILS_color.load(OOMP.tagDetails)
src.tag.OOMP_tag_DETAILS_desc.load(OOMP.tagDetails)
src.tag.OOMP_tag_DETAILS_index.load(OOMP.tagDetails)
