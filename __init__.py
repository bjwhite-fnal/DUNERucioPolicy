from .path_gen import construct_surl_dune_sam, construct_surl_dune_metacat
from .lfn2pfn import lfn2pfn_DUNE

SUPPORTED_VERSION = ["1.29", "1.30", "1.31", "32"]

def get_algorithms():
    return { 'lfn2pfn': { 'DUNE': lfn2pfn_DUNE }, 'surl': { 'DUNE_sam': construct_surl_dune_sam,
                                                            'DUNE_metacat': construct_surl_dune_metacat } }
