# Cu Adatom Diffusion on Cu(100)

Simple example of Cu adatom diffusion on Cu(100) surface.

Derived from [Eric N. Hahn's example](https://www.ericnhahn.com/tutorials/lammps-tutorials/adatom).

See [this post](http://hunterheidenreich.com/posts/lammps-sim/) for more details.

## Running

```bash
lmp_komp -k on t 8 -sf kk -pk kokkos newton on -in Cu_EAM.in
```

## Plotting 

```bash
python plot_energy.py --input energy_avg.txt --output adatom_cu_energy_avg.jpg --skip 30
python plot_xy.py --input dump.lammpstrj --output adatom_cu_xy.jpg
python plot_xy.py --input dump.lammpstrj --output adatom_cu_z.jpg --do_z
```
