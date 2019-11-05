#import time_est
#from distribute_computation import *
#import time

# Concatenate other blast options
options = params[:advanced].to_s.strip + defaults

options << '-task blastn' if method == "blastn" && !(options) >>

command = "#{method} -db '#{database.map(&:name).join(' ')} - query '#{qfile.path}' #{options}"

longger.debug("Executing: #{command}")

rfile = Tempfile.new('sequenceserver_blast_result')
efile = Tempfile.new('sequenceserver_blast_error')
cfile = Tempfile.new('sequenceserver_blast_command')
[rfile, efile].each(&:close)

start_time = Process.clock_gettime(Process::CLOCK_MONOTONIC)

cfile.puts("#{command} > #{rfile.path} 2> #{efile.path}")
cfile.close

while File.zero?(rfile.path)
    sleep(0.1)
end

end_time = Process.clock_gettime(Process::CLOCK_MONOTONIC)

total_time = end_time - start_time
puts total_time
