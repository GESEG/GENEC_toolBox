# GENEC_toolBox

GENEC_toolBox is meant to help you handling the files generated by the Geneva stellar evolution code or the SYCLIST tool. It processes the files and provides the possibility to plot any variable as a function of any other one.

Requires:
 - numpy >= 1.10
 - scipy >= 0.19
 - matplotlib >= 2.0

# CHANGES:

v. 8.2.0:
 * Gaia colours are included
 * colour_corr can be applied to all mags and colours
 * new variable t_rel which goes from 0 to 1 during MS, from 1 to 2 during He-b, and from 2 to 3 during advanced stages. BEWARE: in Kippen it is not yet possible to draw the burning zones with this x axis.
 * xline and yline now accept argument lw=float for line width
 * old_hirschi format accepted for evolution and structure files
 * loadEFromDir accepts now wa=True
 * closest_line now displays the model for which the closest line is printed in case more than one model is plotted

v. 8.1.0:
 * loadE() can now read the evolution files generated by STAREVOL
 * wa loaded earlier, so Si included in limits of burning phases

v. 8.0.1:
 * if g and H_P are all 0, computes now their values before computing other stuff
 * num_deb and num_fin passed to read_wa()
 * correction of a bug that removed the last line from loadE()
 * addition of ProgPath in config file

v. 8.0:
First public release, forked from Origin_Tools.
