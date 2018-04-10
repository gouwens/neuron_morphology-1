#!/usr/bin/python
# To Do: This will need to be revisited once the morphology summary class is refactored


import argschema as ags
from allensdk.neuron_morphology._schemas import MorphologySummaryParameters
import allensdk.core.json_utilities as ju
import allensdk.neuron_morphology.rendering.reconstruction_thumbnail as ms
import allensdk.neuron_morphology.swc as swc
from PIL import Image


def draw_cortex_thumbnail(morphology_summary, image_file, pia_transform):

    cortex_width = 200
    cortex_height = 400

    img = Image.new("RGBA", (cortex_width, cortex_height))
    morphology_summary.draw_cortex_thumbnail(img, cortex_width, cortex_height, 0, pia_transform)
    img.save(image_file)


def draw_thumbnail(morphology_summary, image_file, pia_transform, scale, offset, scalebar):

    cell_width = 67 * scale
    height = 90 * scale
    histogram_width = 23 * scale
    total_width = cell_width + histogram_width

    img = Image.new("RGBA", (total_width, height))
    morphology_summary.draw_thumbnail(img, cell_width, height, histogram_width, pia_transform, offset, scalebar)
    img.save(image_file)


def run_morphology_summary(pia_transform, relative_soma_depth, soma_depth, swc_file, thumbnail_file
                           , cortex_thumbnail_file, high_resolution_thumbnail_file):

    morphology = swc.read_swc(swc_file)
    morphology_summary = ms.MorphologySummary(morphology, soma_depth, relative_soma_depth)

    draw_cortex_thumbnail(morphology_summary, cortex_thumbnail_file, pia_transform)
    #draw_thumbnail(morphology_summary, thumbnail_file,  pia_transform, 1, 0, scalebar=True)
    #draw_thumbnail(morphology_summary, high_resolution_thumbnail_file, pia_transform, 5, 0, scalebar=False)


def main():

    module = ags.ArgSchemaParser(schema_type=MorphologySummaryParameters)
    run_morphology_summary(module.args["pia_transform"],
                           module.args["relative_soma_depth"],
                           module.args["soma_depth"],
                           module.args["swc_file"],
                           module.args["thumbnail_file"],
                           module.args["cortex_thumbnail_file"],
                           module.args["high_resolution_thumbnail_file"])

    ju.write(module.args["output_json"], {})


if __name__ == "__main__":
    main()
