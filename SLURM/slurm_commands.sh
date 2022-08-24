sbatch start_slurm_job.sh

srun [ -b, --begin ][ -c, --cpus-per-task ][ -d, --dependency ][ -e, --error ][ -J, --job-name ][ --mem ][ --mem-per-cpu ][ -n, --ntasks ][ --ntasks-per-core ][ -o, --output ][ --pty ]

seff <job_id>

scancel <job_id>
