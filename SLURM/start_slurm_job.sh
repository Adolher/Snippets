#!/bin/bash
#
# comments starting with "#SBATCH" will be treated as slurm parameters
#
#SBATCH --ntasks 1                      # run 1 tasks / job steps in parallel
#SBATCH -c 6                            # each of the main tasks requires 6 cores
#SBATCH --mem-per-cpu 200M               # 20M memory per CPU (1200 MB per task)
#SBATCH --time 1440                       # runtime limit 1440 minutes
#SBATCH -o /data/pt_02682/MRI_MPILMBB_LEMON/logs/%j.out        # redirect the output of our job to the given file
#SBATCH -e /data/pt_02682/MRI_MPILMBB_LEMON/logs/%j.err        # redirect stderr to the given file


echo "--ntasks 1"
echo "-c 6"
echo "--mem-per-cpu 200M"
echo "--time 1440"
echo "-o /data/pt_02682/MRI_MPILMBB_LEMON/logs/%j.out"
echo "-o /data/pt_02682/MRI_MPILMBB_LEMON/logs/%j.err"
echo ""
# check on how many nodes resources were allocated for our jobs (depends on the requested resources)
echo "Number of nodes: $SLURM_JOB_NUM_NODES"

# run the hostname command for each allocated task to get the name of the node
for x in seq 1 $SLURM_NTASKS
  do
    srun -n 1 hostname &
  done
wait
echo ""
# start 4 job steps
# since we have requested 2 tasks for our job and each job step needs one task (-n 1), 2 job steps will run in parallel and the others will wait for them to finish.
#
# Important: we have to make sure that the job steps are not using all resources of a specific type. Otherwise they will not run in parallel. By requesting 1 task per job step (-n 1) each job step gets 12 cores and 12 GB memory. Mind that if you used --mem instead of --mem-per-cpu in the job definition you would also have to specify the required amount of memory.


srun -n 1 singularity run --cleanenv micapipe-v0.1.2.simg -sub 010002 -out ./MRI_MPILMBB_LEMON/derivatives -bids ./MRI_MPILMBB_LEMON/MRI_Raw -ses 01 -proc_structural -nocleanup


# wait for background jobs to finish
wait
