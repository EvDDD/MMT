                        appList = []
                        cmd = 'powershell "gps | where {$_.MainWindowTitle } | select ProcessName,Id"'
                        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                        for line in proc.stdout:
                            parts = line.decode().split()
                            if len(parts) >= 2 and parts[1].isdigit():
                                processName = parts[0]
                                processId = int(parts[1])
                                process = psutil.Process(processId)
                                numThreads = process.num_threads()
                                appList.append(f"{processName}|{processId}|{numThreads}")

                        # Convert the list of processes to JSON
                        process_json = json.dumps(appList)

                        # Send the JSON string to the client
                        client_socket.send(process_json.encode())