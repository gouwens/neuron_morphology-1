from typing import NamedTuple


class ReferenceLayerDepths(NamedTuple):
    """ Reference (e.g. average across specimens and regions) depths of 
    cortical layer boundaries. Depths are given from pia. Units are not 
    specified, but the user should ensure they are consistent with other 
    positional and size units (e.g. node positions and radii, point depths). 
    Several features in this package specify defaults in microns; if you 
    provide reference layer depths in other units, you should review features 
    which use these depths and ensure that any default values agree with your 
    units.

    Attributes
    ----------
    pia_side : the (average) depth of the upper surface of the layer
    wm_side : the (average) depth of the lower (closer to white matter) surface
        of the layer
    scale : if True, these depths are taken as describing the upper and lower 
        surfaces of a real feature of the data. If False, one or both of them 
        is taken to represent a user-selected boundary. In the latter case, 
        features such as the layer histograms will not attempt to rescale point 
        depths based on observed local layer thicknesses.

    """

    pia_side: float
    wm_side: float
    scale: bool = True

    @property
    def thickness(self):
        return self.wm_side - self.pia_side


DEFAULT_HUMAN_ME_MET_REFERENCE_LAYER_DEPTHS = {
    "1": ReferenceLayerDepths(0.0, 247.9338740595),
    "2": ReferenceLayerDepths(247.9338740595, 410.0775480852),
    "3": ReferenceLayerDepths(410.0775480852, 1322.3048788711),
    "4": ReferenceLayerDepths(1322.3048788711, 1557.8034331092),
    "5": ReferenceLayerDepths(1557.8034331092, 2189.3775739155),
    "6": ReferenceLayerDepths(2189.3775739155, 3077.3662871205),
    "wm": ReferenceLayerDepths(3077.3662871205, 3277.3662871205, False)
}

DEFAULT_MOUSE_ME_MET_REFERENCE_LAYER_DEPTHS = {
    "1": ReferenceLayerDepths(0.0, 115.1112491335),
    r"2/3": ReferenceLayerDepths(115.1112491335, 333.4658190171),
    "4": ReferenceLayerDepths(333.4658190171, 453.6227158132),
    "5": ReferenceLayerDepths(453.6227158132, 687.6482650269),
    "6a": ReferenceLayerDepths(687.6482650269, 883.1308910545),
    "6b": ReferenceLayerDepths(883.1308910545, 922.5861720311),
    "wm": ReferenceLayerDepths(922.5861720311, 1122.5861720311, False)
}

DEFAULT_MOUSE_REFERENCE_LAYER_DEPTHS = {
    "1": ReferenceLayerDepths(0.0, 116.8406715462),
    r"2/3": ReferenceLayerDepths(116.8406715462, 349.9050202564),
    "4": ReferenceLayerDepths(349.9050202564, 477.8605504893),
    "5": ReferenceLayerDepths(477.8605504893, 717.1835081307),
    "6a": ReferenceLayerDepths(717.1835081307, 909.8772394508),
    "6b": ReferenceLayerDepths(909.8772394508, 957.0592130899),
    "wm": ReferenceLayerDepths(957.0592130899, 1157.0592130899, False)
}

DEFAULT_HUMAN_MTG_REFERENCE_LAYER_DEPTHS = {
    "1": ReferenceLayerDepths(0.0, 247.2137476577),
    "2": ReferenceLayerDepths(247.2137476577, 407.2001623338),
    "3": ReferenceLayerDepths(407.2001623338, 1363.9197375716),
    "4": ReferenceLayerDepths(1363.9197375716, 1610.9787635587),
    "5": ReferenceLayerDepths(1610.9787635587, 2272.5330387742),
    "6": ReferenceLayerDepths(2272.5330387742, 3162.1973826021),
    "wm": ReferenceLayerDepths(3162.1973826021, 3362.1973826021, False)
}

# note that these are in microns!
WELL_KNOWN_REFERENCE_LAYER_DEPTHS = {
    "human_mtg": DEFAULT_HUMAN_MTG_REFERENCE_LAYER_DEPTHS,
    "mouse": DEFAULT_MOUSE_REFERENCE_LAYER_DEPTHS,
    "human_me_met": DEFAULT_HUMAN_ME_MET_REFERENCE_LAYER_DEPTHS,
    "mouse_me_met": DEFAULT_MOUSE_ME_MET_REFERENCE_LAYER_DEPTHS
}
