### Long-Running Command with Async and Polling

```yaml
---
- name: Example Playbook with long-running sleep task
  hosts: all
  become: yes
  tasks:

    - name: Start long-running sleep task
      command: sleep 60   # Simulating a long-running task with sleep for 60 seconds
      async: 65           # Allow up to 65 seconds for the task to complete
      poll: 0             # Do not wait for it to complete, continue with the next task
      register: sleep_job

    - name: Perform other tasks while sleep is running
      command: echo "Executing other tasks while waiting..."
      # Additional tasks that can be performed while the sleep command is running in the background

    - name: Check the status of the sleep task
      async_status:
        jid: "{{ sleep_job.ansible_job_id }}"
      register: sleep_result
      until: sleep_result.finished    # Continue until the sleep task is finished
      retries: 5                      # Number of retries to check the status
      delay: 15                       # Delay between retries (in seconds)

    - name: Confirm completion of the long-running task
      debug:
        msg: "The long-running task has completed."
      when: sleep_result.finished
```

### Explanation

1. **Start a Long-Running Process**:
   - This task runs the command `/bin/sleep 300`, which simulates a long-running task by sleeping for 5 minutes. It is allowed up to 10 minutes to complete (`async: 600`), and Ansible will poll every 10 seconds (`poll: 10`) to check its status.

2. **Check the Status of the Long-Running Task**:
   - The `async_status` module checks the status of the long-running task using the job ID from the previous task. It retries every 10 seconds up to 10 minutes (`retries: 60`, `delay: 10`) until the task is finished.

3. **Report the Result**:
   - Finally, this task uses the `debug` module to display the result of the long-running task, showing the return code (`rc`).
