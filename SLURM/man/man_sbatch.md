# sbatch(1)
Submit a batch script to Slurm.

## description
sbatch  submits  a batch script to Slurm.  The batch script may be given to sbatch through a file name on the command line, or if no file name is specified, sbatch will read in a
script from standard input. The batch script may contain options preceded with "#SBATCH" before any executable commands in  the  script.   sbatch  will  stop  processing  further
\#SBATCH directives once the first non-comment non-whitespace line has been reached in the script.
sbatch  exits immediately after the script is successfully transferred to the Slurm controller and assigned a Slurm job ID.  The batch script is not necessarily granted resources
immediately, it may sit in the queue of pending jobs for some time before its required resources become available.
By default both standard output and standard error are directed to a file of the name "slurm-%j.out", where the "%j" is replaced with the job allocation number. The file will  be
generated on the first node of the job allocation.  Other than the batch script itself, Slurm does no movement of user files.
When the job allocation is finally granted for the batch script, Slurm runs a single copy of the batch script on the first node in the set of allocated nodes.
The following document describes the influence of various options on the allocation of cpus to jobs and tasks.
https://slurm.schedmd.com/cpu_management.html

## return value
sbatch will return 0 on success or error code on failure.

## usage
sbatch [OPTIONS(0)...] [ : [OPTIONS(N)...]] script(0) [args(0)...]

## options
short | long | description
---| --- | ---
-a  | --array=\<indexes> | Submit  a  job array, multiple jobs to be executed with identical parameters.  The indexes specification identifies what array index values should be used. Multiple values may be specified using a comma separated list and/or a range of values with a "-" separator. For example, "--array=0-15" or "--array=0,6,16-32".  A step function can  also be  specified  with  a suffix containing a colon and number. For example, "--array=0-15:4" is equivalent to "--array=0,4,8,12".  A maximum number of simultaneously running tasks from the job array may be specified using a "%" separator.  For example "--array=0-15%4" will limit the number of simultaneously running tasks from this job array to 4.   The minimum index value is 0.  the maximum value is one less than the configuration parameter MaxArraySize.  NOTE: currently, federated job arrays only run on the lo‐ cal cluster.
-A  | --account=\<account> | Charge resources used by this job to specified account.  The account is an arbitrary string. The account name may be changed after job submission using the  scontrol  command.
    | --acctg-freq | Define  the  job accounting and profiling sampling intervals.  This can be used to override the JobAcctGatherFrequency parameter in Slurm's configuration file, slurm.conf. The supported format is as follows:<br><br><dl><dt>--acctg-freq=\<datatype>=\<interval></dt><dd>where \<datatype>\<interval> specifies the task sampling interval  for  the  jobacct_gather  plugin  or  a  sampling  interval  for  a  profiling  type  by  the acct_gather_profile plugin. Multiple, comma-separated \<datatype>=\<interval> intervals may be specified. Supported datatypes are as follows:</dd></dl><dl><dt> task=\<interval></dt><dd>  where  \<interval>  is  the  task  sampling  interval in seconds for the jobacct_gather plugins and for task profiling by the acct_gather_profile plugin. NOTE: This frequency is used to monitor memory usage. If memory limits are enforced the highest frequency a user can request is what  is  configured  in the slurm.conf file.  They can not turn it off (=0) either.</dd><dt> energy=\<interval></dt><dd> where \<interval> is the sampling interval in seconds for energy profiling using the acct_gather_energy plugin</dd><dt> network=\<interval></dt><dd>  where \<interval> is the sampling interval in seconds for infiniband profiling using the acct_gather_interconnect plugin.</dd><dt> filesystem=\<interval></dt><dd> where \<interval> is the sampling interval in seconds for filesystem profiling using the acct_gather_filesystem plugin.</dd></dl> The default value for the task sampling interval is 30 seconds. The  default  value for all other intervals is 0.  An interval of 0 disables sampling of the specified type.  If the task sampling interval is 0, accounting information is collected only at job termination (reducing Slurm interference with the job). Smaller (non-zero) values have a greater impact upon job performance, but a value of 30 seconds is not likely to be noticeable for applications  having  less  than  10,000 tasks.
-B  | --extra-node-info=\<sockets[:cores[:threads]]> | Restrict  node selection to nodes with at least the specified number of sockets, cores per socket and/or threads per core.  NOTE: These options do not specify the resource allocation size.  Each value specified is considered a minimum.  An asterisk (\*) can be used as a placeholder indicating that all available resources of that type  are  to be utilized. Values can also be specified as min-max. The individual levels can also be specified in separate options if desired: <br><br><dl><dd>--sockets-per-node=\<sockets></dd><dd> --cores-per-socket=\<cores></dd><dd> --threads-per-core=\<threads></dd></dl>If task/affinity plugin is enabled, then specifying an allocation in this manner also results in subsequently launched tasks being bound to threads if the -B option specifies a thread count, otherwise an option of cores if a core count is specified, otherwise an option of sockets.  If SelectType is configured to  select/cons_res,  it  must have  a  parameter  of  CR_Core,  CR_Core_Memory,  CR_Socket,  or  CR_Socket_Memory  for  this  option to be honored.  If not specified, the scontrol show job will display 'ReqS:C:T=\*:\*:\*'. This option applies to job allocations.  NOTE: This option is mutually exclusive with --hint, --threads-per-core and --ntasks-per-core.
    | --batch=\<list> | Nodes can have features assigned to them by the Slurm administrator.  Users can specify which of these features are required by their batch script using this options.  For example  a  job's  allocation  may include both Intel Haswell and KNL nodes with features "haswell" and "knl" respectively.  On such a configuration the batch script would normally benefit by executing on a faster Haswell node.  This would be specified using the option "--batch=haswell".  The specification can include AND  and  OR  operators using  the  ampersand  and vertical bar separators. For example: "--batch=haswell|broadwell" or "--batch=haswell|big_memory".  The --batch argument must be a subset of the job's --constraint=\<list> argument (i.e. the job can not request only KNL nodes, but require the script to execute on a Haswell node).  If the request can not be satisfied from the resources allocated to the job, the batch script will execute on the first node of the job allocation.
    | --bb=\<spec> | Burst  buffer  specification.  The  form  of the specification is system dependent.  Note the burst buffer may not be accessible from a login node, but require that salloc spawn a shell on one of its allocated compute nodes.
    | --bbf=\<file_name> | Path of file containing burst buffer specification.  The form of the specification is system dependent.  These burst buffer directives will be inserted into the  submitted batch script.
-b  | --begin=\<time> | Submit the batch script to the Slurm controller immediately, like normal, but tell the controller to defer the allocation of the job until the specified time. Time  may  be  of  the form HH:MM:SS to run a job at a specific time of day (seconds are optional).  (If that time is already past, the next day is assumed.)  You may also specify midnight, noon, fika (3 PM) or teatime (4 PM) and you can have a time-of-day suffixed with AM or PM for running in the morning or the evening.  You  can  also  say  what day the job will be run, by specifying a date of the form MMDDYY or MM/DD/YY YYYY-MM-DD. Combine date and time using the following format YYYY-MM-DD[THH:MM[:SS]]. You can also give times like now + count time-units, where the time-units can be seconds (default), minutes, hours, days, or weeks and you can tell Slurm to run the job  today with the keyword today and to run the job tomorrow with the keyword tomorrow.  The value may be changed after job submission using the scontrol command.  For example:  <br><br><dl><dd>--begin=16:00</dd><dd>--begin=now+1hour</dd><dd>--begin=now+60 (seconds by default)</dd><dd>--begin=2010-01-20T12:34:00</dd></dl> Notes on date/time specifications:<dl><dd>-  Although the 'seconds' field of the HH:MM:SS time specification is allowed by the code, note that the poll time of the Slurm scheduler is not precise enough to guarantee dispatch of the job on the exact second.  The job will be eligible to start on the next poll following the specified time. The exact poll interval depends on the Slurm scheduler (e.g., 60 seconds with the default sched/builtin).</dd><dd>- If no time (HH:MM:SS) is specified, the default is (00:00:00).</dd><dd>-  If a date is specified without a year (e.g., MM/DD) then the current year is assumed, unless the combination of MM/DD and HH:MM:SS has already passed for that year, in which case the next year is used.</dd></dl>
    | --cluster-constraint=[!]\<list> | Specifies features that a federated cluster must have to have a sibling job submitted to it. Slurm will attempt to submit a sibling job to a cluster if it has at least one of the specified features. If the "!" option is included, Slurm will attempt to submit a sibling job to a cluster that has none of the specified features.
    | --comment=\<string> | An arbitrary comment enclosed in double quotes if using spaces or some special characters.
-C  | --constraint=\<list> | Nodes  can  have  features  assigned  to them by the Slurm administrator.  Users can specify which of these features are required by their job using the constraint option. Only nodes having features matching the job constraints will be used to satisfy the request.  Multiple constraints may be specified with AND,  OR,  matching  OR,  resource counts, etc. (some operators are not supported on all system types).  Supported constraint options include:<br><br><dl><dt>Single Name</dt><dd>Only nodes which have the specified feature will be used.  For example, --constraint="intel"</dd><dt>Node Count</dt><dd>A  request  can  specify  the  number  of  nodes needed with some feature by appending an asterisk and count after the feature name.  For example, --nodes=16 --constraint="graphics\*4 ..."  indicates that the job requires 16 nodes and that at least four of those nodes must have the feature "graphics."</dd><dt>AND</dt><dd>If only nodes with all of specified features will be used.  The ampersand is used for an AND operator.  For example, --constraint="intel\&gpu"</dd><dt>OR</dt><dd>If only nodes with at least one of specified features will be used.  The vertical bar is used for an OR operator.  For example, --constraint="intel|amd"</dd><dt>Matching OR</dt><dd>If only one of a set of possible options should be used for all allocated nodes, then use the OR operator and enclose the options within square brackets.  For example, --constraint="[rack1|rack2|rack3|rack4]" might be used to specify that all nodes must be allocated on a single rack of the cluster, but any of those four racks can be used.</dd><dt>Multiple Counts</dt><dd>Specific counts of multiple resources may be specified by using  the  AND  operator  and  enclosing  the  options  within  square  brackets.   For  example,  --con‐straint="[rack1\*2&rack2\*4]"  might  be used to specify that two nodes must be allocated from nodes with the feature of "rack1" and four nodes must be allocated from nodes with the feature "rack2". NOTE: This construct does not support multiple Intel KNL NUMA or MCDRAM modes. For  example,  while  --constraint="[(knl&quad)\*2&(knl&hemi)\*4]"  is  not  supported, --constraint="[haswell\*2&(knl&hemi)\*4]" is supported.  Specification of multiple KNL modes requires the use of a heterogeneous job.</dd><dt>Brackets</dt><dd>Brackets  can  be  used  to  indicate  that  you  are  looking for a set of nodes with the different requirements contained within the brackets. For example, --constraint="[(rack1|rack2)\*1&(rack3)\*2]" will get you one node with either the "rack1" or "rack2" features and two nodes with the "rack3" feature.   The  same  request without the brackets will try to find a single node that meets those requirements.</dd><dt>Parenthesis</dt><dd>Parenthesis  can  be  used  to group like node features together. For example, --constraint="[(knl&snc4&flat)\*4&haswell\*1]" might be used to specify that four nodes with the features "knl", "snc4" and "flat" plus one node with the feature "haswell" are required. All options within parenthesis should be grouped  with  AND  (e.g. "&") operands.</dd></dl>
    | --contiguous | If set, then the allocated nodes must form a contiguous set. NOTE: If SelectPlugin=cons_res this option won't be honored with the topology/tree or topology/3d_torus plugins, both of which can modify the node ordering.
    | --cores-per-socket=\<cores> | Restrict node selection to nodes with at least the specified number of cores per socket.  See additional information under -B option above when task/affinity plugin is enabled.
    | --cpu-freq =\<p1[-p2[:p3]]> | Request that job steps initiated by srun commands inside this sbatch script be run at some requested frequency if possible, on the CPUs selected for the step on  the  compute node(s).<br><b>p1</b>  can  be   [####  \|  low  \|  medium  \|  high  \| highm1] which will set the frequency scaling_speed to the corresponding value, and set the frequency scaling_governor to UserSpace. See below for definition of the values.<br><b>p1</b> can be [Conservative \| OnDemand \| Performance \| PowerSave] which will set the scaling_governor to the corresponding value. The governor has to be in the list set by the slurm.conf option CpuFreqGovernors.<br>When <b>p2</b> is present, p1 will be the minimum scaling frequency and p2 will be the maximum scaling frequency.<br><b>p2</b> can be  [#### \| medium \| high \| highm1] p2 must be greater than p1.<br><b>p3</b> can be [Conservative \| OnDemand \| Performance \| PowerSave \| UserSpace] which will set the governor to the corresponding value.<br>If  <b>p3</b>  is  UserSpace, the frequency scaling_speed will be set by a power or energy aware scheduling strategy to a value between p1 and p2 that lets the job run within the site's power goal. The job may be delayed if p1 is higher than a frequency that allows the job to run within the goal.<br>If the current frequency is \< min, it will be set to min. Likewise, if the current frequency is > max, it will be set to max.<br>Acceptable values at present include:<table><tr><td>####</td><td>frequency in kilohertz</td></tr><tr><td>Low</td><td>the lowest available frequency</td></tr> <tr><td>High</td><td>the highest available frequency</td></tr><tr><td>HighM1</td><td>(high minus one) will select the next highest available frequency</td></tr><tr><td>Medium</td><td>attempts to set a frequency in the middle of the available range</td></tr><tr><td>Conservative</td><td>attempts to use the Conservative CPU governor</td></tr><tr><td>OnDemand</td><td>attempts to use the OnDemand CPU governor (the default value)</td></tr><tr><td>Performance</td><td>attempts to use the Performance CPU governor</td></tr><tr><td>PowerSave</td><td>attempts to use the PowerSave CPU governor</td></tr><tr><td>UserSpace</td><td>attempts to use the UserSpace CPU governor</td></tr></table> The following informational environment variable is set in the job step when --cpu-freq option is requested. SLURM_CPU_FREQ_REQ<br>This environment variable can also be used to supply the value for the CPU frequency request if it is set when the 'srun' command is issued.  The --cpu-freq on the command line  will override the environment variable value.  The form on the environment variable is the same as the command line.  See the ENVIRONMENT VARIABLES section for a description of the SLURM_CPU_FREQ_REQ variable.<br>NOTE: This parameter is treated as a request, not a requirement.  If the job step's node does not support setting the CPU frequency, or the requested value is outside  the bounds of the legal frequencies, an error is logged, but the job step is allowed to continue. <br>NOTE:  Setting  the  frequency for just the CPUs of the job step implies that the tasks are confined to those CPUs.  If task confinement (i.e., TaskPlugin=task/affinity or TaskPlugin=task/cgroup with the "ConstrainCores" option) is not configured, this parameter is ignored. <br>NOTE: When the step completes, the frequency and governor of each selected CPU is reset to the previous values. <br>NOTE: When submitting jobs with  the --cpu-freq option with linuxproc as the ProctrackType can cause jobs to run too quickly before Accounting is able to poll for job  information. As a result not all of accounting information will be present.
    | --cpus-per-gpu=\<ncpus> | Advise Slurm that ensuing job steps will require ncpus processors per allocated GPU.  Not compatible with the --cpus-per-task option.
-c  | --cpus-per-task=\<ncpus> | Advise  the  Slurm  controller  that ensuing job steps will require ncpus number of processors per task.  Without this option, the controller will just try to allocate one processor per task. For instance, consider an application that has 4 tasks, each requiring 3 processors.  If our cluster is comprised of quad-processors nodes and we simply ask for 12 processors,  the  controller  might give us only 3 nodes.  However, by using the --cpus-per-task=3 options, the controller knows that each task requires 3 processors on the same node, and the controller will grant an allocation of 4 nodes, one for each of the 4 tasks.
    | --deadline=\<OPT> | remove the job if no ending is possible before this deadline (start > (deadline - time[-min])).  Default is no deadline.  Valid time formats are: <dl><dd>HH:MM[:SS] [AM\|PM]</dd><dd> MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]</dd><dd> MM/DD[/YY]-HH:MM[:SS]</dd><dd> YYYY-MM-DD[THH:MM[:SS]]]</dd><dd> now[+count[seconds(default)|minutes|hours|days|weeks]]</dd></dl>
    | --delay-boot=\<minutes> | Do not reboot nodes in order to satisfied this job's feature specification if the job has been eligible to run for less than this time period.  If the job has  waited  for less  than  the  specified period, it will use only nodes which already have the specified features.  The argument is in units of minutes.  A default value may be set by a system administrator using the delay_boot option of the SchedulerParameters configuration parameter in the slurm.conf file, otherwise the default value is zero (no delay).
-d  | --dependency=\<dependency_list> | Defer the start of this job until the specified dependencies have been satisfied completed.  \<dependency_list> is of the form \<type:job_id[:job_id][,type:job_id[:job_id]]> or  \<type:job_id[:job_id][?type:job_id[:job_id]]>.   All dependencies must be satisfied if the "," separator is used.  Any dependency may be satisfied if the "?" separator is used.  Only one separator may be used.  Many jobs can share the same dependency and these jobs may even belong to different  users. The  value may be changed after  job submission  using  the scontrol command.  Dependencies on remote jobs are allowed in a federation.  Once a job dependency fails due to the termination state of a preceding job, the dependent job will never be run, even if the preceding job is requeued and has a different termination state in a subsequent execution. <dl><dt>after:job_id[[+time][:jobid[+time]...]]</dt><dd>After the specified jobs start or are cancelled and 'time' in minutes from job start or cancellation happens, this job can begin execution. If no  'time'  is  given then there is no delay after start or cancellation.</dd><dt>afterany:job_id[:jobid...]</dt><dd> This job can begin execution after the specified jobs have terminated.</dd><dt> afterburstbuffer:job_id[:jobid...]</dt><dd> This job can begin execution after the specified jobs have terminated and any associated burst buffer stage out operations have completed.</dd><dt> aftercorr:job_id[:jobid...]</dt><dd> A task of this job array can begin execution after the corresponding task ID in the specified job has completed successfully (ran to completion with an exit code of zero).</dd><dt> afternotok:job_id[:jobid...]</dt><dd> This job can begin execution after the specified jobs have terminated in some failed state (non-zero exit code, node failure, timed out, etc).</dd><dt> afterok:job_id[:jobid...]</dt><dd> This job can begin execution after the specified jobs have successfully executed (ran to completion with an exit code of zero).</dd><dt> expand:job_id</dt><dd> Resources allocated to this job should be used to expand the specified job.  The job to expand must share the same QOS (Quality of  Service)  and  partition.   Gang scheduling of resources in the partition is also not supported.  "expand" is not allowed for jobs that didn't originate on the same cluster as the submitted job.</dd><dt> singleton</dt><dd> This  job  can begin execution after any previously launched jobs sharing the same job name and user have terminated.  In other words, only one job by that name and owned by that user can be running or suspended at any point in time.  In a federation, a singleton dependency must be fulfilled on all clusters unless DependencyParameters=disable_remote_singleton is used in slurm.conf.</dd></dl>
-D  | --chdir=\<directory> | Set  the  working directory of the batch script to directory before it is executed. The path can be specified as full path or relative path to the directory where the command is executed.
-e  | --error=\<filename pattern> | Instruct Slurm to connect the batch script's standard error directly to the file name specified in the "filename pattern".  By default both standard  output  and  standard error  are directed to the same file.  For job arrays, the default file name is "slurm-%A_%a.out", "%A" is replaced by the job ID and "%a" with the array index.  For other jobs, the default file name is "slurm-%j.out", where the "%j" is replaced by the job ID.  See the filename pattern section below for filename specification options.
    | --exclusive[=user|mcs] | The job allocation can not share nodes with other running jobs (or just other users with the "=user" option or with the "=mcs" option).  The default  shared/exclusive  behavior depends on system configuration and the partition's OverSubscribe option takes precedence over the job's option.
    | --export=\<[ALL,]environment variables\|ALL\|NONE> | Identify which environment variables from the submission environment are propagated to the launched application. Note that SLURM_\* variables are always propagated. <dl><dt>--export=ALL</dt><dd> Default mode if --export is not specified. All of the users environment will be loaded (either from callers environment or clean environment if --get-user-env is specified).</dd><dt> --export=NONE</dt><dd> Only SLURM_\* variables from the user environment will be defined. User must use absolute path to the binary to be executed  that  will  define  the  environment. User can not specify explicit environment variables with NONE.  --get-user-env will be ignored. This  option is particularly important for jobs that are submitted on one cluster and execute on a different cluster (e.g. with different paths).  To avoid steps inheriting environment export settings (e.g. NONE) from sbatch command, the environment variable SLURM_EXPORT_ENV should be set to ALL in the job script.</dd><dt> --export=\<[ALL,]environment variables></dt><dd> Exports all SLURM_\* environment variables along with explicitly defined variables. Multiple environment variable names should be  comma  separated.   Environment variable  names  may be specified to propagate the current value (e.g. "--export=EDITOR") or specific values may be exported (e.g. "--export=EDITOR=/bin/emacs"). If ALL is specified, then all user environment variables will be loaded and will take precedence over any explicitly given environment variables. <br>Example: --export=EDITOR,ARG1=test In this example, the propagated environment will only contain the variable EDITOR from the user's environment, SLURM_\* environment variables, and ARG1=test. <br>Example: --export=ALL,EDITOR=/bin/emacs There are two possible outcomes for this example. If the caller has the EDITOR environment variable defined, then the job's environment will inherit the variable from  the  caller's  environment.   If the caller doesn't have an environment variable defined for EDITOR, then the job's environment will use the value given by --export.</dd></dl>
    | --export-file=\<filename \| fd> | If a number between 3 and OPEN_MAX is specified as the argument to this option, a readable file descriptor will be assumed (STDIN and STDOUT are not supported as valid arguments).  Otherwise a filename is assumed.  Export environment variables defined in \<filename> or read from \<fd> to the job's execution environment. The content is one or more environment variable definitions of the form NAME=value, each separated by a null character.  This allows the use of special characters in environment definitions.
-F  | --nodefile=\<node file> | Much like --nodelist, but the list is contained in a file of name node file.  The node names of the list may also span multiple lines in the file.    Duplicate node  names in the file will be ignored.  The order of the node names in the list is not important; the node names will be sorted by Slurm.
    | --get-user-env[=timeout][mode] | This  option  will  tell sbatch to retrieve the login environment variables for the user specified in the --uid option.  The environment variables are retrieved by running something of this sort "su - \<username> -c /usr/bin/env" and parsing the output.  Be aware that any environment variables already set in  sbatch's  environment  will  take precedence  over  any  environment  variables in the user's login environment. Clear any environment variables before calling sbatch that you do not want propagated to the spawned program.  The optional timeout value is in seconds. Default value is 8 seconds.  The optional mode value control the "su" options.  With a mode value of "S",  "su" is  executed  without  the "-" option.  With a mode value of "L", "su" is executed with the "-" option, replicating the login environment.  If mode not specified, the mode established at Slurm build time is used.  Example of use include "--get-user-env", "--get-user-env=10" "--get-user-env=10L", and "--get-user-env=S".
    | --gid=\<group> | If sbatch is run as root, and the --gid option is used, submit the job with group's group access permissions.  group may be the group name or the numerical group ID.
-G  | --gpus=[\<type>:]\<number> | Specify the total number of GPUs required for the job.  An optional GPU type specification can be supplied.  For example "--gpus=volta:3".  Multiple  options  can  be  requested in a comma separated list, for example: "--gpus=volta:3,kepler:1".  See also the --gpus-per-node, --gpus-per-socket and --gpus-per-task options.
    | --gpu-bind=[verbose,]\<type> | Bind  tasks to specific GPUs.  By default every spawned task can access every GPU allocated to the job.  If "verbose," is specified before \<type>, then print out GPU binding information. <br>Supported type options:<dl><dt>closest</dt><dd>Bind each task to the GPU(s) which are closest.  In a NUMA environment, each task may be bound to more than one GPU (i.e.  all GPUs in that NUMA environment).</dd><dt> map_gpu:\<list></dt><dd> Bind by setting GPU masks on tasks (or ranks) as specified where \<list> is \<gpu_id_for_task_0>,\<gpu_id_for_task_1>,... GPU IDs are interpreted as decimal  values unless they are preceded with '0x' in which case they interpreted as hexadecimal values. If the number of tasks (or ranks) exceeds the number of elements in this list, elements in the list will be reused as needed starting from the beginning of the list. To simplify support for large task counts, the lists  may  follow  a map  with  an  asterisk and repetition count.  For example "map_gpu:0\*4,1\*4".  If the task/cgroup plugin is used and ConstrainDevices is set in cgroup.conf, then the GPU IDs are zero-based indexes relative to the GPUs allocated to the job (e.g. the first GPU is 0, even if the global ID is 3). Otherwise, the  GPU  IDs  are global IDs, and all GPUs on each node in the job should be allocated for predictable binding results.</dd><dt> mask_gpu:\<list></dt><dd> Bind  by  setting  GPU masks on tasks (or ranks) as specified where \<list> is \<gpu_mask_for_task_0>,\<gpu_mask_for_task_1>,... The mapping is specified for a node and identical mapping is applied to the tasks on every node (i.e. the lowest task ID on each node is mapped to the first mask specified in the list,  etc.).  GPU masks  are  always interpreted as hexadecimal values but can be preceded with an optional '0x'. To simplify support for large task counts, the lists may follow a map with an asterisk and repetition count.  For example "mask_gpu:0x0f\*4,0xf0\*4".  If the task/cgroup plugin is used and ConstrainDevices is set in  cgroup.conf, then  the  GPU IDs are zero-based indexes relative to the GPUs allocated to the job (e.g. the first GPU is 0, even if the global ID is 3). Otherwise, the GPU IDs are global IDs, and all GPUs on each node in the job should be allocated for predictable binding results.</dd><dt> single:\<tasks_per_gpu></dt><dd> Like --gpu-bind=closest, except that each task can only be bound to a single GPU, even when it can be bound to multiple GPUs that are equally close.  The GPU  to bind  to is determined by \<tasks_per_gpu>, where the first \<tasks_per_gpu> tasks are bound to the first GPU available, the second \<tasks_per_gpu> tasks are bound to the second GPU available, etc.  This is basically a block distribution of tasks onto available GPUs, where the available GPUs are  determined  by  the  socket affinity of the task and the socket affinity of the GPUs as specified in gres.conf's Cores parameter.</dd></dl>
    | --gpu-freq=[\<type]=value>[,\<type=value>][,verbose] | Request  that  GPUs allocated to the job are configured with specific frequency values.  This option can be used to independently configure the GPU and its memory frequencies.  After the job is completed, the frequencies of all affected GPUs will be reset to the highest possible values.  In some cases, system power caps  may  override  the requested  values.   The  field  type  can  be  "memory".   If type is not specified, the GPU frequency is implied.  The value field can either be "low", "medium", "high", "highm1" or a numeric value in megahertz (MHz).  If the specified numeric value is not possible, a value as close as possible will be used. See below for definition of the values.  The verbose option causes current GPU frequency information to be logged.  Examples of use include "--gpu-freq=medium,memory=high" and "--gpu-freq=450".<br> Supported value definitions:<dl><dt> low</dt><dd> the lowest available frequency.</dd><dt> medium</dt><dd>    attempts to set a frequency in the middle of the available range.</dd><dt> high</dt><dd> the highest available frequency.</dd><dt> highm1</dt><dd> (high minus one) will select the next highest available frequency.</dd></dl>
    | --gpus-per-node=[\<type>:]\<number> | Specify  the  number of GPUs required for the job on each node included in the job's resource allocation.  An optional GPU type specification can be supplied.  For example "--gpus-per-node=volta:3".  Multiple options can be requested  in  a  comma  separated  list,  for  example:  "--gpus-per-node=volta:3,kepler:1".   See  also  the  --gpus, --gpus-per-socket and --gpus-per-task options.
    | --gpus-per-socket=[\<type>:]\<number> | Specify the number of GPUs required for the job on each socket included in the job's resource allocation.  An optional GPU type specification can be supplied.  For example "--gpus-per-socket=volta:3".  Multiple options can be requested in a comma separated list, for example: "--gpus-per-socket=volta:3,kepler:1".  Requires job  to  specify  a sockets per node count ( --sockets-per-node).  See also the --gpus, --gpus-per-node and --gpus-per-task options.
    | --gpus-per-task=[\<type>:]\<number> | Specify  the number of GPUs required for the job on each task to be spawned in the job's resource allocation.  An optional GPU type specification can be supplied.  For example "--gpus-per-task=volta:1". Multiple options can be requested in a comma separated  list,  for  example:  "--gpus-per-task=volta:3,kepler:1".  See  also  the  --gpus, --gpus-per-socket  and  --gpus-per-node  options.   This option requires an explicit task count, e.g. -n, --ntasks or "--gpus=X --gpus-per-task=Y" rather than an ambiguous range of nodes with -N, --nodes. NOTE: This option will not have any impact on GPU binding, specifically it won't limit the number of devices set for CUDA_VISIBLE_DEVICES.
    | --gres=\<list> | Specifies a comma delimited list of generic consumable resources.  The format of each entry on the list is "name[[:type]:count]".  The name is that of the  consumable  resource.   The count is the number of those resources with a default value of 1.  The count can have a suffix of "k" or "K" (multiple of 1024), "m" or "M" (multiple of 1024 x 1024), "g" or "G" (multiple of 1024 x 1024 x 1024), "t" or "T" (multiple of 1024 x 1024 x 1024 x 1024), "p" or "P" (multiple of 1024 x 1024 x 1024 x 1024 x  1024).   The specified  resources  will be allocated to the job on each node.  The available generic consumable resources is configurable by the system administrator.  A list of available generic consumable resources will be printed and  the  command  will  exit  if  the  option  argument  is  "help".   Examples  of  use  include  "--gres=gpu:2,mic:1", "--gres=gpu:kepler:2", and "--gres=help".
    | --gres-flags=\<type> | Specify generic resource task binding options. <dl><dt>disable-binding</dt><dd> Disable  filtering of CPUs with respect to generic resource locality.  This option is currently required to use more CPUs than are bound to a GRES (i.e. if a GPU is bound to the CPUs on one socket, but resources on more than one socket are required to run the job).  This option may permit a job to be allocated resources  sooner than otherwise possible, but may result in lower job performance. NOTE: This option is specific to SelectType=cons_res.</dd><dt> enforce-binding</dt><dd> The  only CPUs available to the job will be those bound to the selected GRES (i.e. the CPUs identified in the gres.conf file will be strictly enforced). This option may result in delayed initiation of a job.  For example a job requiring two GPUs and one CPU will be delayed until both GPUs on a single socket are available rather than  using  GPUs bound to separate sockets, however, the application performance may be improved due to improved communication speed.  Requires the node to be configured with more than one socket and resource filtering will be performed on a per-socket basis. NOTE: This option is specific to SelectType=cons_tres.</dd></dl>
-H  | --hold | Specify the job is to be submitted in a held state (priority of zero).  A held job can now be released using  scontrol  to  reset  its  priority  (e.g.  "scontrol  release \<job_id>").
-h  | --help | Display help information and exit.
    | --hint=\<type> | Bind tasks according to application hints.<br> NOTE:  This  option  cannot be used in conjunction with --ntasks-per-core, --threads-per-core or -B. If --hint is specified as a command line argument, it will take precedence over the environment. <dl><dt>compute_bound</dt><dd> Select settings for compute bound applications: use all cores in each socket, one thread per core.</dd><dt> memory_bound</dt><dd> Select settings for memory bound applications: use only one core in each socket, one thread per core.</dd><dt> [no]multithread</dt><dd> [don't] use extra threads with in-core multi-threading which can benefit communication intensive applications.  Only supported with the task/affinity plugin.</dd><dt> help</dt><dd> show this help message</dd></dl>
    | --ignore-pbs | Ignore all "#PBS" and "#BSUB" options specified in the batch script.
-i  | --input=\<filename pattern> | Instruct Slurm to connect the batch script's standard input directly to the file name specified in the "filename pattern". By default, "/dev/null" is open on the batch script's standard input and both standard output and standard error are directed to a file of the name  "slurm-%j.out",  where the "%j" is replaced with the job allocation number, as described below in the filename pattern section.
-J  | --job-name=\<jobname> | Specify a name for the job allocation. The specified name will appear along with the job id number when querying running jobs on the system. The default is the name of the batch script, or just "sbatch" if the script is read on sbatch's standard input.
-k  | --no-kill [=off] | Do not automatically terminate a job if one of the nodes it has been allocated fails.  The user will assume the responsibilities for fault-tolerance should  a  node  fail. When  there is a node failure, any active job steps (usually MPI jobs) on that node will almost certainly suffer a fatal error, but with --no-kill, the job allocation will not be revoked so the user may launch new job steps on the remaining nodes in their allocation. Specify an optional argument of "off" disable the effect of the SBATCH_NO_KILL environment variable. By default Slurm terminates the entire job allocation if any node fails in its range of allocated nodes.
    | --kill-on-invalid-dep=\<yes\|no> | If a job has an invalid dependency and it can never run this parameter tells Slurm to terminate it or not. A terminated job state will be JOB_CANCELLED.  If this option is not  specified  the  system  wide  behavior  applies.   By default the job stays pending with reason DependencyNeverSatisfied or if the kill_invalid_depend is specified in slurm.conf the job is terminated.
-L  | --licenses=\<license> | Specification of licenses (or other resources available on all nodes of the cluster) which must be allocated to this job.  License names can be followed  by  a  colon  and count  (the default count is one).  Multiple license names should be comma separated (e.g.  "--licenses=foo:4,bar").  To submit jobs using remote licenses, those served by the slurmdbd, specify the name of the server providing the licenses.  For example "--license=nastran@slurmdb:12".
-M  | --clusters=\<string> | Clusters to issue commands to.  Multiple cluster names may be comma separated.  The job will be submitted to the one cluster providing the earliest expected job initiation time. The default value is the current cluster. A value of 'all' will query to run on all clusters.  Note the --export option to control environment variables exported between clusters.  Note that the SlurmDBD must be up for this option to work properly.
-m  | --distribution=arbitrary\|\<block\|cyclic\|plane=\<options>[:block\|cyclic\|fcyclic]> | Specify alternate distribution methods for remote processes.  In sbatch, this only sets environment variables that will be used by subsequent srun requests.   This  option controls  the  assignment  of  tasks to the nodes on which resources have been allocated, and the distribution of those resources to tasks for binding (task affinity). The first distribution method (before the ":") controls the distribution of resources across nodes. The optional second distribution method (after the ":") controls  the  distribution  of  resources  across  sockets  within  a node.  Note that with select/cons_res, the number of cpus allocated on each socket and node may be different. Refer to https://slurm.schedmd.com/mc_support.html for more information on resource allocation, assignment of tasks to nodes, and binding of tasks to CPUs.<br> First distribution method:<br><dl><dt> block</dt><dd>  The block distribution method will distribute tasks to a node such that consecutive tasks share a node. For example, consider an allocation of three nodes each with two  cpus.  A four-task block distribution request will distribute those tasks to the nodes with tasks one and two on the first node, task three on the second node, and task four on the third node.  Block distribution is the default behavior if the number of tasks exceeds the number of allocated nodes.</dd><dt> cyclic</dt><dd> The cyclic distribution method will distribute tasks to a node such that consecutive tasks are distributed over consecutive nodes (in a  round-robin  fashion).  For example,  consider  an allocation of three nodes each with two cpus. A four-task cyclic distribution request will distribute those tasks to the nodes with tasks one and four on the first node, task two on the second node, and task three on the third node.  Note that when SelectType is select/cons_res, the same  number  of  CPUs may  not be allocated on each node. Task distribution will be round-robin among all the nodes with CPUs yet to be assigned to tasks.  Cyclic distribution is the default behavior if the number of tasks is no larger than the number of allocated nodes.</dd><dt> plane</dt><dd>  The tasks are distributed in blocks of a specified size. The number of tasks distributed to each node is the same as for cyclic distribution, but  the  taskids  assigned  to each node depend on the plane size. Additional distribution specifications cannot be combined with this option.  For more details (including examples and diagrams), please see https://slurm.schedmd.com/mc_support.html and https://slurm.schedmd.com/dist_plane.html</dd><dt> arbitrary</dt><dd> The arbitrary method of distribution will allocate processes in-order as listed in file designated by the environment variable SLURM_HOSTFILE.  If this variable  is listed  it  will override any other method specified.  If not set the method will default to block.  Inside the hostfile must contain at minimum the number of hosts requested and be one per line or comma separated.  If specifying a task count (-n, --ntasks=\<number>), your tasks will be laid out on the nodes in the order of  the file. NOTE:  The  arbitrary distribution option on a job allocation only controls the nodes to be allocated to the job and not the allocation of CPUs on those nodes. This option is meant primarily to control a job step's task layout in an existing job allocation for the srun command.</dd></dl> <br>Second distribution method:<br><dl><dt> block</dt><dd>  The block distribution method will distribute tasks to sockets such that consecutive tasks share a socket.</dd><dt> cyclic</dt><dd> The cyclic distribution method will distribute tasks to sockets such that consecutive tasks are distributed over consecutive sockets  (in  a  round-robin  fashion). Tasks requiring more than one CPU will have all of those CPUs allocated on a single socket if possible.</dd><dt> fcyclic</dt><dd> The  fcyclic  distribution  method will distribute tasks to sockets such that consecutive tasks are distributed over consecutive sockets (in a round-robin fashion). Tasks requiring more than one CPU will have each CPUs allocated in a cyclic fashion across sockets.</dd></dl>
    | --mail-type=\<type> | Notify user by email when certain event types occur.  Valid type values are NONE, BEGIN, END, FAIL, REQUEUE, ALL (equivalent to BEGIN, END, FAIL, INVALID_DEPEND,  REQUEUE, and  STAGE_OUT),  INVALID_DEPEND  (dependency never satisfied), STAGE_OUT (burst buffer stage out and teardown completed), TIME_LIMIT, TIME_LIMIT_90 (reached 90 percent of time limit), TIME_LIMIT_80 (reached 80 percent of time limit), TIME_LIMIT_50 (reached 50 percent of time limit) and ARRAY_TASKS (send emails for each array task).   Multiple type values may be specified in a comma separated list.  The user to be notified is indicated with --mail-user.  Unless the ARRAY_TASKS option is specified, mail notifications on job BEGIN, END and FAIL apply to a job array as a whole rather than generating individual email messages for each task in the job array.
    | --mail-user=\<user> | User to receive email notification of state changes as defined by --mail-type.  The default value is the submitting user.
    | --mcs-label=\<mcs> | Used only when the mcs/group plugin is enabled.  This parameter is a group among the groups of the user.  Default value is calculated by the Plugin mcs if it's enabled.
    | --mem=\<size[units]> | Specify the real memory required per node.  Default units are megabytes.  Different units can be specified using the suffix [K\|M\|G\|T].  Default value is DefMemPerNode  and the  maximum  value  is  MaxMemPerNode. If configured, both parameters can be seen using the scontrol show config command.  This parameter would generally be used if whole nodes are allocated to jobs (SelectType=select/linear).  Also see --mem-per-cpu and --mem-per-gpu.  The --mem, --mem-per-cpu and --mem-per-gpu options are mutually  exclusive. If --mem, --mem-per-cpu or --mem-per-gpu are specified as command line arguments, then they will take precedence over the environment. <br>NOTE: A memory size specification of zero is treated as a special case and grants the job access to all of the memory on each node.  If the job is allocated multiple nodes in a heterogeneous cluster, the memory limit on each node will be that of the node in the allocation with the smallest memory size (same limit will apply to every node  in the job's allocation). <br>NOTE:  Enforcement  of memory limits currently relies upon the task/cgroup plugin or enabling of accounting, which samples memory use on a periodic basis (data need not be stored, just collected). In both cases memory use is based upon the job's Resident Set Size (RSS). A task may exceed the memory limit until the  next  periodic  accounting sample.
    | --mem-per-cpu=\<size[units]> | Minimum memory required per allocated CPU.  Default units are megabytes.  The default value is DefMemPerCPU and the maximum value is MaxMemPerCPU (see exception below). If configured, both parameters can be seen using the scontrol show config command.  Note that if the job's --mem-per-cpu value exceeds the configured MaxMemPerCPU,  then  the user's limit will be treated as a memory limit per task; --mem-per-cpu will be reduced to a value no larger than MaxMemPerCPU; --cpus-per-task will be set and the value of --cpus-per-task multiplied by the new --mem-per-cpu value will equal the original --mem-per-cpu value specified by the user.  This parameter would generally be used if individual processors are allocated to jobs (SelectType=select/cons_res).  If resources are allocated by core, socket, or whole nodes, then the number of CPUs allocated to a job may be higher than the task count and the value of --mem-per-cpu should be adjusted accordingly.  Also see --mem  and  --mem-per-gpu.   The  --mem,  --mem-per-cpu  and --mem-per-gpu options are mutually exclusive. <br>NOTE:  If the final amount of memory requested by a job can't be satisfied by any of the nodes configured in the partition, the job will be rejected.  This could happen if --mem-per-cpu is used with the --exclusive option for a job allocation and --mem-per-cpu times the number of CPUs on a node is greater than the total memory of that node.
    | --mem-per-gpu=\<size[units]> | Minimum memory required per allocated GPU.  Default units are megabytes.  Different units can be specified using the suffix [K\|M\|G\|T].  Default value is  DefMemPerGPU  and is  available  on  both  a  global and per partition basis.  If configured, the parameters can be seen using the scontrol show config and scontrol show partition commands. Also see --mem.  The --mem, --mem-per-cpu and --mem-per-gpu options are mutually exclusive.
    | --mem-bind=[{quiet,verbose},]type | Bind tasks to memory. Used only when the task/affinity plugin is enabled and the NUMA memory functions are available. Note that the resolution of CPU and  memory  binding may  differ  on  some  architectures.  For example, CPU binding may be performed at the level of the cores within a processor while memory binding will be performed at the level of nodes, where the definition of "nodes" may differ from system to system.  By default no memory binding is performed; any task using any CPU can  use  any  memory. This  option  is typically used to ensure that each task is bound to the memory closest to its assigned CPU. The use of any type other than "none" or "local" is not recommended. <br>NOTE: To have Slurm always report on the selected memory binding for all commands executed in a shell, you can enable verbose mode by setting the  SLURM_MEM_BIND  environment variable value to "verbose".<br> The following informational environment variables are set when --mem-bind is in use:<br> <dl><dd>SLURM_MEM_BIND_LIST</dd><dd> SLURM_MEM_BIND_PREFER</dd><dd> SLURM_MEM_BIND_SORT</dd><dd> SLURM_MEM_BIND_TYPE</dd><dd> SLURM_MEM_BIND_VERBOSE</dd></dl> See the ENVIRONMENT VARIABLES section for a more detailed description of the individual SLURM_MEM_BIND\* variables.<br> Supported options include:<br><dl><dt> help</dt><dd>   show this help message</dd><dt> local</dt><dd>  Use memory local to the processor in use</dd><dt> map_mem:\<list></dt><dd> Bind by setting memory masks on tasks (or ranks) as specified where \<list> is \<numa_id_for_task_0>,\<numa_id_for_task_1>,...  The mapping is specified for a node and identical mapping is applied to the tasks on every node (i.e. the lowest task ID on each node is mapped to the first ID specified in the list, etc.).  NUMA IDs  are interpreted  as  decimal  values unless they are preceded with '0x' in which case they interpreted as hexadecimal values.  If the number of tasks (or ranks) exceeds the number of elements in this list, elements in the list will be reused as needed starting from the beginning of the list.  To  simplify  support  for  large  task counts,  the lists may follow a map with an asterisk and repetition count.  For example "map_mem:0x0f\*4,0xf0\*4".  For predictable binding results, all CPUs for each node in the job should be allocated to the job.</dd><dt> mask_mem:\<list></dt><dd>  Bind by setting memory masks on tasks (or ranks) as specified where \<list> is \<numa_mask_for_task_0>,\<numa_mask_for_task_1>,...  The mapping is specified for a node and  identical  mapping  is applied to the tasks on every node (i.e. the lowest task ID on each node is mapped to the first mask specified in the list, etc.).  NUMA masks are always interpreted as hexadecimal values.  Note that masks must be preceded with a '0x' if they don't begin with [0-9] so they are seen as numerical  values.   If  the  number of tasks (or ranks) exceeds the number of elements in this list, elements in the list will be reused as needed starting from the beginning of the list.  To simplify support for large task counts, the lists may follow a mask with an asterisk and repetition count.  For example "mask_mem:0\*4,1\*4".  For  predictable binding results, all CPUs for each node in the job should be allocated to the job.</dd><dt> no[ne] don't bind tasks to memory (default)</dd><dt> p[refer]</dt><dd> Prefer use of first specified NUMA node, but permit use of other available NUMA nodes.</dd><dt> q[uiet]</dt><dd> quietly bind before task runs (default)</dd><dt> rank</dt><dd>   bind by task rank (not recommended)</dd><dt> sort</dt><dd>   sort free cache pages (run zonesort on Intel KNL nodes)</dd><dt> v[erbose]</dt><dd> verbosely report binding before task runs</dd></dl>
    | --mincpus=\<n> | Specify a minimum number of logical cpus/processors per node.
-N  | --nodes=\<minnodes[-maxnodes]> | Request  that  a  minimum  of minnodes nodes be allocated to this job.  A maximum node count may also be specified with maxnodes.  If only one number is specified, this is used as both the minimum and maximum node count.  The partition's node limits supersede those of the job.  If a job's node limits are outside of the  range  permitted  for its  associated  partition,  the job will be left in a PENDING state.  This permits possible execution at a later time, when the partition limit is changed.  If a job node limit exceeds the number of nodes configured in the partition, the job will be rejected.  Note that the environment variable SLURM_JOB_NODES will be set to  the  count  of nodes actually allocated to the job. See the ENVIRONMENT VARIABLES  section for more information.  If -N is not specified, the default behavior is to allocate enough nodes to satisfy the requirements of the -n and -c options.  The job will be allocated as many nodes as possible within the range specified and without delaying  the  initiation of  the  job.  The node count specification may include a numeric value followed by a suffix of "k" (multiplies numeric value by 1,024) or "m" (multiplies numeric value by 1,048,576).
-n  | --ntasks=\<number> | sbatch does not launch tasks, it requests an allocation of resources and submits a batch script. This option advises the Slurm controller that job steps run within the allocation  will  launch  a maximum of number tasks and to provide for sufficient resources.  The default is one task per node, but note that the --cpus-per-task option will change this default.
    | --network=\<type> | Specify information pertaining to the switch or network.  The interpretation of type is system dependent.  This option is supported when running Slurm on a Cray  natively. It is used to request using Network Performance Counters.  Only one value per request is valid.  All options are case in-sensitive.  In this configuration supported values include:<br><dl><dt> system</dt><dd> Use the system-wide network performance counters. Only nodes requested will be marked in use for the job allocation.  If the job does not fill up the  entire  system the  rest  of the nodes are not able to be used by other jobs using NPC, if idle their state will appear as PerfCnts.  These nodes are still available for other jobs not using NPC. </dd><dt>blade</dt><dd> Use the blade network performance counters. Only nodes requested will be marked in use for the job allocation.  If the job does not fill up the entire blade(s) allocated  to  the  job those blade(s) are not able to be used by other jobs using NPC, if idle their state will appear as PerfCnts.  These nodes are still available for other jobs not using NPC.</dd></dl> In all cases the job allocation request must specify the --exclusive option.  Otherwise the request will be denied.<br> Also with any of these options steps are not allowed to share blades, so resources would remain idle inside an allocation if the step running on a blade does not  take  up all the nodes on the blade.<br> The  network option is also supported on systems with IBM's Parallel Environment (PE).  See IBM's LoadLeveler job command keyword documentation about the keyword "network" for more information.  Multiple values may be specified in a comma separated list.  All options are case in-sensitive.  Supported values include:<br><dl><dt> BULK_XFER[=\<resources>]</dt><dd> Enable bulk transfer of data using Remote Direct-Memory Access (RDMA).  The optional resources specification is a numeric value which can have a suffix of "k", "K", "m", "M", "g" or "G" for kilobytes, megabytes or gigabytes.  NOTE: The resources specification is not supported by the underlying IBM infrastructure as of Parallel Environment version 2.2 and no value should be specified at this time.</dd><dt> CAU=\<count></dt><dd> Number of Collective Acceleration Units (CAU) required.  Applies only to IBM Power7-IH processors.  Default value is zero.  Independent CAU will  be  allocated for each programming interface (MPI, LAPI, etc.)</dd><dt> DEVNAME=\<name></dt><dd> Specify the device name to use for communications (e.g. "eth0" or "mlx4_0").</dd><dt> DEVTYPE=\<type></dt><dd> Specify  the  device  type to use for communications.  The supported values of type are: "IB" (InfiniBand), "HFI" (P7 Host Fabric Interface), "IPONLY" (IP-Only interfaces), "HPCE" (HPC Ethernet), and "KMUX" (Kernel Emulation of HPCE).  The devices allocated to a job must all be of the same type.  The default value depends upon depends upon what hardware is available and in order of preferences is IPONLY (which is not considered in User Space mode), HFI, IB, HPCE, and KMUX.</dd><dt> IMMED =\<count></dt><dd> Number of immediate send slots per window required.  Applies only to IBM Power7-IH processors.  Default value is zero.</dd><dt> INSTANCES =\<count></dt><dd> Specify number of network connections for each task on each network connection.  The default instance count is 1.</dd><dt> IPV4</dt><dd>        Use Internet Protocol (IP) version 4 communications (default).</dd><dt> IPV6</dt><dd>        Use Internet Protocol (IP) version 6 communications.</dd><dt> LAPI</dt><dd>        Use the LAPI programming interface.</dd><dt> MPI</dt><dd>         Use the MPI programming interface.  MPI is the default interface.</dd><dt> PAMI</dt><dd>        Use the PAMI programming interface.</dd><dt> SHMEM</dt><dd>       Use the OpenSHMEM programming interface.</dd><dt> SN_ALL</dt><dd>      Use all available switch networks (default).</dd><dt> SN_SINGLE</dt><dd>   Use one available switch network.</dd><dt> UPC</dt><dd>         Use the UPC programming interface.</dd><dt> US</dt><dd>          Use User Space communications.</dd></dl><br> Some examples of network specifications:<br><dl><dt> Instances=2,US,MPI,SN_ALL</dt><dd> Create two user space connections for MPI communications on every switch network for each task.</dd><dt> US,MPI,Instances=3,Devtype=IB</dt><dd> Create three user space connections for MPI communications on every InfiniBand network for each task.</dd><dt> IPV4,LAPI,SN_Single</dt><dd> Create a IP version 4 connection for LAPI communications on one switch network for each task.</dd><dt> Instances=2,US,LAPI,MPI</dt><dd> Create  two  user space connections each for LAPI and MPI communications on every switch network for each task. Note that SN_ALL is the default option so every switch network is used. Also note that Instances=2 specifies that two connections are established for each protocol (LAPI and MPI) and each task.  If there are two networks and four tasks on the node then a total of 32 connections are established (2 instances x 2 protocols x 2 networks x 4 tasks).</dd></dl>
    | --nice[=adjustment] | Run  the  job  with an adjusted scheduling priority within Slurm. With no adjustment value the scheduling priority is decreased by 100. A negative nice value increases the priority, otherwise decreases it. The adjustment range is +/- 2147483645. Only privileged users can specify a negative adjustment.
    | --no-requeue | Specifies that the batch job should never be requeued under any circumstances.  Setting this option will prevent system administrators from being able to restart  the  job (for  example, after a scheduled downtime), recover from a node failure, or be requeued upon preemption by a higher priority job.  When a job is requeued, the batch script is initiated from its beginning.  Also see the --requeue option.  The JobRequeue configuration parameter controls the default behavior on the cluster.
    | --ntasks-per-core=\<ntasks> | Request the maximum ntasks be invoked on each core.  Meant to be used with the --ntasks option.  Related to --ntasks-per-node except at the core level instead of the  node level.  NOTE: This option is not supported unless SelectType=cons_res is configured (either directly or indirectly on Cray systems) along with the node's core count.
    | --ntasks-per-gpu=\<ntasks> | Request  that there are ntasks tasks invoked for every GPU.  This option can work in two ways: 1) either specify --ntasks in addition, in which case a type-less GPU specification will be automatically determined to satisfy --ntasks-per-gpu, or 2) specify the GPUs wanted (e.g. via --gpus or --gres) without specifying --ntasks, and the total task  count  will be automatically determined.  The number of CPUs needed will be automatically increased if necessary to allow for any calculated task count.  This option will implicitly set --gpu-bind=single:\<ntasks>, but that can be overridden with an explicit --gpu-bind specification.  This option is not  compatible  with  a  node  range (i.e.  -N\<minnodes-maxnodes>).   This  option is not compatible with --gpus-per-task, --gpus-per-socket, or --ntasks-per-node.  This option is not supported unless Select‐Type=cons_tres is configured (either directly or indirectly on Cray systems).
    | --ntasks-per-node=\<ntasks> | Request that ntasks be invoked on each node.  If used with the --ntasks option, the --ntasks option will take precedence and the --ntasks-per-node will  be  treated  as  a maximum  count of tasks per node.  Meant to be used with the --nodes option.  This is related to --cpus-per-task=ncpus, but does not require knowledge of the actual number of cpus on each node.  In some cases, it is more convenient to be able to request that no more than a specific number of tasks be invoked on each node.  Examples  of  this include submitting a hybrid MPI/OpenMP app where only one MPI "task/rank" should be assigned to each node while allowing the OpenMP portion to utilize all of the parallelism present in the node, or submitting a single setup/cleanup/monitoring job to each node of a pre-existing allocation as one step in a larger job script.
    | --ntasks-per-socket=\<ntasks> | Request the maximum ntasks be invoked on each socket.  Meant to be used with the --ntasks option.  Related to --ntasks-per-node except at the socket level instead  of  the node  level.   NOTE:  This  option  is  not supported unless SelectType=cons_res is configured (either directly or indirectly on Cray systems) along with the node's socket count.
-O  | --overcommit | Overcommit resources.  When applied to job allocation, only one CPU is allocated to the job per node and options used to specify the number  of  tasks  per  node,  socket, core,  etc.   are ignored.  When applied to job step allocations (the srun command when executed within an existing job allocation), this option can be used to launch more than one task per CPU.  Normally, srun will not allocate more than one process per CPU.  By specifying --overcommit you are explicitly allowing more than one  process  per CPU. However no more than MAX_TASKS_PER_NODE tasks are permitted to execute per node.  NOTE: MAX_TASKS_PER_NODE is defined in the file slurm.h and is not a variable, it is set at Slurm build time.
-o  | --output=\<filename pattern> | Instruct Slurm to connect the batch script's standard output directly to the file name specified in the "filename pattern".  By default both standard output  and  standard error  are directed to the same file.  For job arrays, the default file name is "slurm-%A_%a.out", "%A" is replaced by the job ID and "%a" with the array index.  For other jobs, the default file name is "slurm-%j.out", where the "%j" is replaced by the job ID.  See the filename pattern section below for filename specification options.
    | --open-mode=append\|truncate | Open the output and error files using append or truncate mode as specified.  The default value is specified by the system configuration parameter JobFileAppend.
    | --parsable | Outputs only the job id number and the cluster name if present.  The values are separated by a semicolon. Errors will still be displayed.
-p  | --partition=\<partition_names> | Request a specific partition for the resource allocation.  If not specified, the default behavior is to allow the slurm controller to select the default partition as  designated by the system administrator. If the job can use more than one partition, specify their names in a comma separate list and the one offering earliest initiation will be used with no regard given to the partition name ordering (although higher priority partitions will be considered first).  When the job is initiated,  the  name  of  the partition used will be placed first in the job record partition string.
    | --power=\<flags> | Comma separated list of power management plugin options.  Currently available flags include: level (all nodes allocated to the job should have identical power caps, may be disabled by the Slurm configuration option PowerParameters=job_no_level).
    | --priority=\<value> | Request a specific job priority.  May be subject to configuration specific constraints.  value should either be a numeric value or  "TOP"  (for  highest  possible  value). Only Slurm operators and administrators can set the priority of a job.
    | --profile=\<all\|none\|[energy[,\|task[,\|lustre[,\|network]]]]> | enables  detailed  data  collection  by the acct_gather_profile plugin.  Detailed data are typically time-series that are stored in an HDF5 file for the job or an InfluxDB database depending on the configured plugin.<table><tr><td> All</td><td> All data types are collected. (Cannot be combined with other values.)</td></tr><tr><td> None</td><td> No data types are collected. This is the default. (Cannot be combined with other values.)</td></tr><tr><td> Energy</td><td> Energy data is collected.</td></tr><tr><td> Task</td><td> Task (I/O, Memory, ...) data is collected.</td></tr><tr><td> Lustre</td><td>    Lustre data is collected.</td></tr><tr><td> Network</td><td>   Network (InfiniBand) data is collected.</td></tr></table>
    | --propagate[=rlimit[,rlimit...]] | Allows users to specify which of the modifiable (soft) resource limits to propagate to the compute nodes and apply to their jobs. If no rlimit is specified, then  all  resource limits will be propagated.  The following rlimit names are supported by Slurm (although some options may not be supported on some systems):<table><tr><td> ALL</td><td> All limits listed below (default)</td></tr><tr><td> NONE</td><td> No limits listed below</td></tr><tr><td> AS</td><td> The maximum address space for a process</td></tr><tr><td> CORE</td><td> The maximum size of core file</td></tr><tr><td> CPU</td><td> The maximum amount of CPU time</td><7tr><tr><td> DATA</td><td> The maximum size of a process's data segment</td></tr><tr><td> FSIZE</td><td> The  maximum  size  of  files created. Note that if the user sets FSIZE to less than the current size of the slurmd.log, job launches will fail with a 'File size limit exceeded' error.</td></tr><tr><td> MEMLOCK</td><td> The maximum size that may be locked into memory</td></tr><tr><td> NOFILE</td><td> The maximum number of open files</td></tr><tr><td> NPROC</td><td> The maximum number of processes available</td></tr><tr><td> RSS</td><td> The maximum resident set size</td></tr><tr><td> STACK</td><td> The maximum stack size</td></tr></table>
-q  | --qos=\<qos> | Request a quality of service for the job.  QOS values can be defined for each user/cluster/account association in the Slurm database.  Users will be limited to their association's defined set of qos's when the Slurm configuration parameter, AccountingStorageEnforce, includes "qos" in its definition.
-Q  | --quiet | Suppress informational messages from sbatch such as Job ID. Only errors will still be displayed.
    | --reboot | Force  the  allocated  nodes  to reboot before starting the job.  This is only supported with some system configurations and will otherwise be silently ignored. Only root, SlurmUser or admins can reboot nodes.
    | --requeue | Specifies that the batch job should be eligible for requeuing.  The job may be requeued explicitly by a system administrator, after node failure, or upon preemption  by  a higher  priority job.  When a job is requeued, the batch script is initiated from its beginning.  Also see the --no-requeue option.  The JobRequeue configuration parameter controls the default behavior on the cluster.
    | --reservation=\<reservation_names> | Allocate resources for the job from the named reservation. If the job can use more than one reservation, specify their names in a comma separate list and the one  offering earliest  initiation.  Each  reservation will be considered in the order it was requested.  All reservations will be listed in scontrol/squeue through the life of the job. In accounting the first reservation will be seen and after the job starts the reservation used will replace it.
-s  | --oversubscribe | The job allocation can over-subscribe resources with other running jobs.  The resources to be over-subscribed can be nodes, sockets, cores, and/or  hyperthreads  depending upon  configuration.   The default over-subscribe behavior depends on system configuration and the partition's OverSubscribe option takes precedence over the job's option. This option may result in the allocation being granted sooner than if the --oversubscribe option was not set and allow higher system utilization, but  application  performance will likely suffer due to competition for resources.  Also see the --exclusive option.
-S  | --core-spec=\<num> | Count  of  specialized  cores  per  node  reserved  by the job for system operations and not used by the application. The application will not use these cores, but will be charged for their allocation.  Default value is dependent upon the node's configured CoreSpecCount value.  If a value of zero is designated and the Slurm configuration option AllowSpecResourcesUsage is enabled, the job will be allowed to override CoreSpecCount and use the specialized resources on nodes it is allocated.  This option can not be used with the --thread-spec option.
    | --signal=[[R][B]:]\<sig_num>[@\<sig_time>] | When a job is within sig_time seconds of its end time, send it the signal sig_num.  Due to the resolution of event handling by Slurm, the signal may be sent up to 60  seconds  earlier  than specified.  sig_num may either be a signal number or name (e.g. "10" or "USR1").  sig_time must have an integer value between 0 and 65535.  By default, no signal is sent before the job's end time.  If a sig_num is specified without any sig_time, the default time will be 60 seconds.  Use the "B:" option to signal only  the batch  shell,  none  of the other processes will be signaled. By default all job steps will be signaled, but not the batch shell itself.  Use the "R:" option to allow this job to overlap with a reservation with MaxStartDelay set.  To have the signal sent at preemption time see the preempt_send_user_signal SlurmctldParameter.
    | --sockets-per-node=\<sockets> | Restrict node selection to nodes with at least the specified number of sockets.  See additional information under -B option above when task/affinity plugin is enabled.
    | --spread-job | Spread the job allocation over as many nodes as possible and attempt to evenly distribute tasks across the allocated nodes.  This option disables the topology/tree plugin.
    | --switches=\<count>[@\<max-time>] | When a tree topology is used, this defines the maximum count of switches desired for the job allocation and optionally  the  maximum  time  to  wait  for  that  number  of switches.  If  Slurm finds an allocation containing more switches than the count specified, the job remains pending until it either finds an allocation with desired switch count or the time limit expires.  It there is no switch count limit, there is no delay in starting the job.  Acceptable time formats include "minutes",  "minutes:seconds", "hours:minutes:seconds",  "days-hours", "days-hours:minutes" and "days-hours:minutes:seconds".  The job's maximum time delay may be limited by the system administrator using the SchedulerParameters configuration parameter with the max_switch_wait parameter option.  On a dragonfly network the only switch count supported is 1 since  communication  performance  will  be highest when a job is allocate resources on one leaf switch or more than 2 leaf switches.  The default max-time is the max_switch_wait SchedulerParameters.
-t  | --time=\<time> | Set a limit on the total run time of the job allocation.  If the requested time limit exceeds the partition's time limit, the job will be left in a PENDING state (possibly indefinitely).   The  default  time  limit  is  the partition's default time limit.  When the time limit is reached, each task in each job step is sent SIGTERM followed by SIGKILL.  The interval between signals is specified by the Slurm configuration parameter KillWait.  The OverTimeLimit configuration parameter may permit  the  job  to  run longer than scheduled.  Time resolution is one minute and second values are rounded up to the next minute. A  time  limit  of  zero  requests  that  no  time  limit be imposed.  Acceptable time formats include "minutes", "minutes:seconds", "hours:minutes:seconds", "days-hours", "days-hours:minutes" and "days-hours:minutes:seconds".
    | --test-only | Validate the batch script and return an estimate of when a job would be scheduled to run given the current job queue and all the other arguments  specifying  the  job  requirements. No job is actually submitted.
    | --thread-spec=\<num> | Count  of  specialized  threads per node reserved by the job for system operations and not used by the application. The application will not use these threads, but will be charged for their allocation.  This option can not be used with the --core-spec option.
    | --threads-per-core=\<threads> | Restrict node selection to nodes with at least the specified number of threads per core. In task layout, use the specified  maximum  number  of  threads  per  core.  NOTE: "Threads"  refers  to the number of processing units on each core rather than the number of application tasks to be launched per core.  See additional information under -B option above when task/affinity plugin is enabled.
    | --time-min=\<time> | Set a minimum time limit on the job allocation.  If specified, the job may have its --time limit lowered to a value no lower than --time-min if doing so permits the job to begin  execution earlier than otherwise possible.  The job's time limit will not be changed after the job is allocated resources.  This is performed by a backfill scheduling algorithm to allocate resources otherwise reserved for higher priority jobs.  Acceptable time formats include  "minutes",  "minutes:seconds",  "hours:minutes:seconds", "days-hours", "days-hours:minutes" and "days-hours:minutes:seconds".
    | --tmp=\<size[units]> | Specify a minimum amount of temporary disk space per node.  Default units are megabytes.  Different units can be specified using the suffix [K|M|G|T].
    | --usage | Display brief help message and exit.
    | --uid=\<user> | Attempt  to submit and/or run a job as user instead of the invoking user id. The invoking user's credentials will be used to check access permissions for the target partition. User root may use this option to run jobs as a normal user in a RootOnly partition for example. If run as root, sbatch will drop its permissions to the uid specified after node allocation is successful. user may be the user name or numerical user ID.
    | --use-min-nodes | If a range of node counts is given, prefer the smaller count.
-V  | --version | Display version information and exit.
-v  | --verbose | Increase the verbosity of sbatch's informational messages.  Multiple -v's will further increase sbatch's verbosity.  By default only errors will be displayed.
-w  | --nodelist=\<node name list> | Request a specific list of hosts.  The job will contain all of these hosts and possibly additional hosts as needed to satisfy resource requirements.  The list may be specified as a comma-separated list of hosts, a range of hosts (host[1-5,7,...] for example), or a filename.  The host list will be assumed to be a filename if it  contains  a "/"  character.   If  you specify a minimum node or processor count larger than can be satisfied by the supplied host list, additional resources will be allocated on other nodes as needed.  Duplicate node names in the list will be ignored.  The order of the node names in the list is not important; the node names will be sorted by Slurm.
-W  | --wait | Do not exit until the submitted job terminates.  The exit code of the sbatch command will be the same as the exit code of the submitted job. If the job terminated due to a signal rather than a normal exit, the exit code will be set to 1.  In the case of a job array, the exit code recorded will be the highest value for any task in the job array.
    | --wait-all-nodes=\<value> | Controls when the execution of the command begins.  By default the job will begin execution as soon as the allocation is made.<br> 0    Begin execution as soon as allocation can be made.  Do not wait for all nodes to be ready for use (i.e. booted). <br>1    Do not begin execution until all nodes are ready for use.
    | --wckey=\<wckey> | Specify wckey to be used with job.  If TrackWCKey=no (default) in the slurm.conf this value is ignored.
    | --wrap=\<command string> | Sbatch will wrap the specified command string in a simple "sh" shell script, and submit that script to the slurm controller.  When --wrap is used, a script name and  arguments may not be specified on the command line; instead the sbatch-generated wrapper script is used.
-x  | --exclude=\<node name list> | Explicitly exclude certain nodes from the resources granted to the job.

## filename pattern
sbatch allows for a filename pattern to contain one or more replacement symbols, which are a percent sign "%" followed by a letter (e.g. %j).

pattern | description
--- | ---
\\\\  | Do not process any of the replacement symbols.
%%    | The character "%".
%A    | Job array's master job allocation number.
%a    | Job array ID (index) number.
%J    | jobid.stepid of the running job. (e.g. "128.0")
%j    | jobid of the running job.
%N    | short hostname. This will create a separate IO file per node.
%n    | Node identifier relative to current job (e.g. "0" is the first node of the running job) This will create a separate IO file per node.
%s    | stepid of the running job.
%t    | task identifier (rank) relative to current job. This will create a separate IO file per task.
%u    | User name.
%x    | Job name.

A  number  placed  between the percent character and format specifier may be used to zero-pad the result inthe IO filename. This number is ignored if the format specifier corresponds to  non-numericdata (%N for example).

Some examples of how the format string may be used for a 4 task job step with a Job ID of 128 andstep id of 0 are included below:

       job%J.out      job128.0.out

       job%4j.out     job0128.out

       job%j-%2t.out  job128-00.out, job128-01.out, ...

## PERFORMANCE
Executing sbatch sends a remote procedure call to slurmctld. If enough calls from sbatch or other Slurm client commands that send remote procedure calls to the  slurmctld  daemoncome in at once, it can result in a degradation of performance of the slurmctld daemon, possibly resulting in a denial of service.

Do  not run sbatch or other Slurm client commands that send remote procedure calls to slurmctld from loops in shell scripts or other programs. Ensure that programs limit calls tosbatch to the minimum necessary for the information you are trying to gather.

## INPUT ENVIRONMENT VARIABLES
Upon startup, sbatch will read and handle the options set in the following environment variables.  Note that environment variables will  override  any  options  set  in  a  batchscript, and command line options will override any environment variables.

       SBATCH_ACCOUNT        Same as -A, --account

       SBATCH_ACCTG_FREQ     Same as --acctg-freq

       SBATCH_ARRAY_INX      Same as -a, --array

       SBATCH_BATCH          Same as --batch

       SBATCH_CLUSTERS       Same as --clusters

       SBATCH_CONSTRAINT     Same as -C, --constraint

       SBATCH_CORE_SPEC      Same as --core-spec

       SBATCH_CPUS_PER_GPU   Same as --cpus-per-gpu

       SBATCH_DEBUG          Same as -v, --verbose

       SBATCH_DELAY_BOOT     Same as --delay-boot

       SBATCH_DISTRIBUTION   Same as -m, --distribution

       SBATCH_EXCLUSIVE      Same as --exclusive

       SBATCH_EXPORT         Same as --export

       SBATCH_GET_USER_ENV   Same as --get-user-env

       SBATCH_GPUS           Same as -G, --gpus

       SBATCH_GPU_BIND       Same as --gpu-bind

       SBATCH_GPU_FREQ       Same as --gpu-freq

       SBATCH_GPUS_PER_NODE  Same as --gpus-per-node

       SBATCH_GPUS_PER_TASK  Same as --gpus-per-task

       SBATCH_GRES           Same as --gres

       SBATCH_GRES_FLAGS     Same as --gres-flags

       SBATCH_HINT           Same as --hint

       SBATCH_IGNORE_PBS     Same as --ignore-pbs

       SBATCH_JOB_NAME       Same as -J, --job-name

       SBATCH_MEM_BIND       Same as --mem-bind

       SBATCH_MEM_PER_CPU    Same as --mem-per-cpu

       SBATCH_MEM_PER_GPU    Same as --mem-per-gpu

       SBATCH_MEM_PER_NODE   Same as --mem

       SBATCH_NETWORK        Same as --network

       SBATCH_NO_KILL        Same as -k, --no-kill

       SBATCH_NO_REQUEUE     Same as --no-requeue

       SBATCH_OPEN_MODE      Same as --open-mode

       SBATCH_OVERCOMMIT     Same as -O, --overcommit

       SBATCH_PARTITION      Same as -p, --partition

       SBATCH_POWER          Same as --power

       SBATCH_PROFILE        Same as --profile

       SBATCH_QOS            Same as --qos

       SBATCH_RESERVATION    Same as --reservation

       SBATCH_REQ_SWITCH     When  a  tree  topology  is used, this defines the maximum count of switches
                             desired for the job allocation and optionally the maximum time to wait for that
                             number of switches. See --switches

       SBATCH_REQUEUE        Same as --requeue

       SBATCH_SIGNAL         Same as --signal

       SBATCH_SPREAD_JOB     Same as --spread-job

       SBATCH_THREAD_SPEC    Same as --thread-spec

       SBATCH_TIMELIMIT      Same as -t, --time

       SBATCH_USE_MIN_NODES  Same as --use-min-nodes

       SBATCH_WAIT           Same as -W, --wait

       SBATCH_WAIT_ALL_NODES Same as --wait-all-nodes

       SBATCH_WAIT4SWITCH    Max time waiting for requested switches. See --switches

       SBATCH_WCKEY          Same as --wckey

       SLURM_CLUSTERS        Same as --clusters

       SLURM_CONF            The location of the Slurm configuration file.

       SLURM_EXIT_ERROR      Specifies the exit code generated when a Slurm error occurs (e.g. invalid options).
                             This can be used by a script to distinguish application exit codes from
                             various Slurm error conditions.

       SLURM_HINT            Same as --hint

       SLURM_STEP_KILLED_MSG_NODE_ID=ID
                             If set, only the specified node will log when the job or step are killed by a signal.

## OUTPUT ENVIRONMENT VARIABLES
The Slurm controller will set the following variables in the environment of the batch script.

       SBATCH_MEM_BIND
              Set to value of the --mem-bind option.

       SBATCH_MEM_BIND_LIST
              Set to bit mask used for memory binding.

       SBATCH_MEM_BIND_PREFER
              Set to "prefer" if the --mem-bind option includes the prefer option.

       SBATCH_MEM_BIND_TYPE
              Set to the memory binding type specified with the --mem-bind option.  Possible values are
              "none", "rank", "map_map", "mask_mem" and "local".

       SBATCH_MEM_BIND_VERBOSE
              Set to "verbose" if the --mem-bind option includes the verbose option.  Set to "quiet" otherwise.

       SLURM_*_HET_GROUP_#
              For a heterogeneous job allocation, the environment variables are set separately for each component.

       SLURM_ARRAY_TASK_COUNT
              Total number of tasks in a job array.

       SLURM_ARRAY_TASK_ID
              Job array ID (index) number.

       SLURM_ARRAY_TASK_MAX
              Job array's maximum ID (index) number.

       SLURM_ARRAY_TASK_MIN
              Job array's minimum ID (index) number.

       SLURM_ARRAY_TASK_STEP
              Job array's index step size.

       SLURM_ARRAY_JOB_ID
              Job array's master job ID number.

       SLURM_CLUSTER_NAME
              Name of the cluster on which the job is executing.

       SLURM_CPUS_ON_NODE
              Number of CPUS on the allocated node.

       SLURM_CPUS_PER_GPU
              Number of CPUs requested per allocated GPU.  Only set if the --cpus-per-gpu option is specified.

       SLURM_CPUS_PER_TASK
              Number of cpus requested per task.  Only set if the --cpus-per-task option is specified.

       SLURM_DIST_PLANESIZE
              Plane distribution size. Only set for plane distributions.  See -m, --distribution.

       SLURM_DISTRIBUTION
              Same as -m, --distribution

       SLURM_EXPORT_ENV
              Same as -e, --export.

       SLURM_GPUS
              Number of GPUs requested.  Only set if the -G, --gpus option is specified.

       SLURM_GPU_BIND
              Requested binding of tasks to GPU.  Only set if the --gpu-bind option is specified.

       SLURM_GPU_FREQ
              Requested GPU frequency.  Only set if the --gpu-freq option is specified.

       SLURM_GPUS_PER_NODE
              Requested GPU count per allocated node.  Only set if the --gpus-per-node option is specified.

       SLURM_GPUS_PER_SOCKET
              Requested GPU count per allocated socket.  Only set if the --gpus-per-socket option is specified.

       SLURM_GPUS_PER_TASK
              Requested GPU count per allocated task.  Only set if the --gpus-per-task option is specified.

       SLURM_GTIDS
              Global task IDs running on this node.  Zero  origin and comma separated.

       SLURM_JOB_ACCOUNT
              Account name associated of the job allocation.

       SLURM_JOB_ID (and SLURM_JOBID for backwards compatibility)
              The ID of the job allocation.

       SLURM_JOB_CPUS_PER_NODE
              Count of processors available to the job on this node.  Note the select/linear plugin allocates
              entire nodes to jobs, so the value indicates the total count of CPUs on the node. The select/cons_res
              plugin allocates individual processors to jobs, so this number indicates the number of processors
              on this node allocated to the job.

       SLURM_JOB_DEPENDENCY
              Set to value of the --dependency option.

       SLURM_JOB_NAME
              Name of the job.

       SLURM_JOB_NODELIST (and SLURM_NODELIST for backwards compatibility)
              List of nodes allocated to the job.

       SLURM_JOB_NUM_NODES (and SLURM_NNODES for backwards compatibility)
              Total number of nodes in the job's resource allocation.

       SLURM_JOB_PARTITION
              Name of the partition in which the job is running.

       SLURM_JOB_QOS
              Quality Of Service (QOS) of the job allocation.

       SLURM_JOB_RESERVATION
              Advanced reservation containing the job allocation, if any.

       SLURM_LOCALID
              Node local task ID for the process within a job.

       SLURM_MEM_PER_CPU
              Same as --mem-per-cpu

       SLURM_MEM_PER_GPU
              Requested memory per allocated GPU.  Only set if the --mem-per-gpu option is specified.

       SLURM_MEM_PER_NODE
              Same as --mem

       SLURM_NODE_ALIASES
              Sets of node name, communication address and hostname for nodes allocated to the job from the cloud.
              Each element in the set if colon separated and each set is comma sepa‐
              rated. For example: SLURM_NODE_ALIASES=ec0:1.2.3.4:foo,ec1:1.2.3.5:bar

       SLURM_NODEID
              ID of the nodes allocated.

       SLURM_NTASKS (and SLURM_NPROCS for backwards compatibility)
              Same as -n, --ntasks

       SLURM_NTASKS_PER_CORE
              Number of tasks requested per core.  Only set if the --ntasks-per-core option is specified.

       SLURM_NTASKS_PER_GPU
              Number of tasks requested per GPU.  Only set if the --ntasks-per-gpu option is specified.

       SLURM_NTASKS_PER_NODE
              Number of tasks requested per node.  Only set if the --ntasks-per-node option is specified.

       SLURM_NTASKS_PER_SOCKET
              Number of tasks requested per socket.  Only set if the --ntasks-per-socket option is specified.

       SLURM_HET_SIZE
              Set to count of components in heterogeneous job.

       SLURM_PRIO_PROCESS
              The  scheduling priority (nice value) at the time of job submission. This value is propagated
              to the spawned processes.

       SLURM_PROCID
              The MPI rank (or relative process ID) of the current process

       SLURM_PROFILE
              Same as --profile

       SLURM_RESTART_COUNT
              If the job has been restarted due to system failure or has been explicitly requeued, this will
              be sent to the number of times the job has been restarted.

       SLURM_SUBMIT_DIR
              The directory from which sbatch was invoked or, if applicable, the directory specified by
              the -D, --chdir option.

       SLURM_SUBMIT_HOST
              The hostname of the computer from which sbatch was invoked.

       SLURM_TASKS_PER_NODE
              Number  of  tasks  to  be initiated on each node. Values are comma separated and in the same order
              as SLURM_JOB_NODELIST.  If two or more consecutive nodes are to have the
              same task count, that count is followed by "(x#)" where "#" is the repetition count. For
              example, "SLURM_TASKS_PER_NODE=2(x3),1" indicates that the first three nodes  will
              each execute two tasks and the fourth node will execute one task.

       SLURM_TASK_PID
              The process ID of the task being started.

       SLURM_TOPOLOGY_ADDR
              This  is set only if the  system  has  the  topology/tree  plugin configured. The value will be
              set to the names network switches which  may be  involved  in  the  job's
              communications from the system's top level switch down to the leaf switch and  ending
              with node name. A period is used to separate each hardware component name.

       SLURM_TOPOLOGY_ADDR_PATTERN
              This is set only if the  system  has  the  topology/tree  plugin configured. The value will be
              set  component  types  listed   in  SLURM_TOPOLOGY_ADDR. Each   component
              will be identified as either "switch" or "node".  A period is  used  to separate
              each hardware component type.

       SLURMD_NODENAME
              Name of the node running the job script.

## EXAMPLES
Specify a batch script by filename on the command line.  The batch script specifies a 1 minute time limit for the job.

              $ cat myscript
              #!/bin/sh
              #SBATCH --time=1
              srun hostname |sort

              $ sbatch -N4 myscript
              salloc: Granted job allocation 65537

              $ cat slurm-65537.out
              host1
              host2
              host3
              host4

Pass a batch script to sbatch on standard input:

              $ sbatch -N4 <<EOF
              > #!/bin/sh
              > srun hostname |sort
              > EOF
              sbatch: Submitted batch job 65541

              $ cat slurm-65541.out
              host1
              host2
              host3
              host4

To create a heterogeneous job with 3 components, each allocating a unique set of nodes:

              sbatch -w node[2-3] : -w node4 : -w node[5-7] work.bash
              Submitted batch job 34987
