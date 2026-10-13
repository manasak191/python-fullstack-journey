Assignment 5: Configure EBS Volume for EC2

AWS services: EC2, Amazon EBS, Linux

1. Objective

To attach additional storage to an EC2 instance, format it, mount it to a directory, and configure automatic mounting after reboot.

2. Important concepts

Amazon EBS: Persistent block storage used with EC2 instances for storing files, application data, and databases.

Volume: A virtual disk that provides storage capacity.

Filesystem: A structure such as ext4 that Linux uses to organize and store files.

Mounting: Making a filesystem accessible through a directory.

/etc/fstab: A Linux configuration file used to define filesystems that should be mounted automatically.

UUID: A unique identifier for a filesystem, useful for identifying a disk consistently.

3. Steps performed

Created a 2 GiB EBS volume with the gp3 volume type.

Attached the volume to the Bastion Host.

Identified the new disk using lsblk.

Formatted the disk using the ext4 filesystem.

Created the /data directory.

Mounted the disk at /data.

Added the volume's UUID to /etc/fstab.

Tested the configuration using umount, mount -a, and df -h.

4. Commands used

Command

	

Purpose




lsblk

	

Lists disks and partitions.




sudo mkfs -t ext4 /dev/nvme1n1

	

Creates an ext4 filesystem on the new disk.




sudo mkdir -p /data

	

Creates the mount directory.




sudo mount /dev/nvme1n1 /data

	

Mounts the disk at /data.




df -h

	

Shows filesystem capacity and usage.




sudo blkid /dev/nvme1n1

	

Displays the filesystem UUID.




sudo cp /etc/fstab /etc/fstab.bak

	

Backs up the mount configuration.




sudo umount /data

	

Unmounts the filesystem.




sudo mount -a

	

Mounts filesystems configured in /etc/fstab.




sudo findmnt --verify

	

Checks mount configuration.

Important: Always verify the device name before formatting. Formatting the wrong disk can destroy data.

5. Final result

Your new volume was successfully mounted:

Device:       /dev/nvme1n1
Size:         2.0 GiB
Filesystem:   ext4
Mount point:  /data

The mount -a test successfully mounted the volume again, confirming that your /etc/fstab entry worked in the test.

6. Interview questions and answers

Q1. What is Amazon EBS?

Amazon Elastic Block Store is a persistent block storage service designed for use with EC2 instances.

Q2. What is the difference between EBS and instance store?

EBS provides persistent storage that exists independently of an instance's running state. Instance store is temporary storage tied to the underlying host and can be lost when the instance stops or terminates, depending on the lifecycle event.

Q3. What is mounting in Linux?

Mounting makes a filesystem accessible through a directory, such as /data.

Q4. What is the purpose of /etc/fstab?

It defines filesystems and mount options so they can be mounted automatically during boot or through commands such as mount -a.

Q5. Why use a UUID instead of a device name?

Device names such as /dev/nvme1n1 can change in some circumstances. A filesystem UUID provides a more reliable way to identify the filesystem.

Q6. What happens if you don't configure /etc/fstab?

A manually mounted filesystem generally won't be mounted automatically after a reboot.

Q7. Can an EBS volume be attached to any EC2 instance?

Normally, the volume must be in the same Availability Zone as the EC2 instance, and the volume type and attachment limits must be supported.

7. Interview project explanation
Writing

I completed an AWS project to configure additional storage for an EC2 instance using Amazon EBS. I created a 2 GiB volume, attached it to the instance, formatted it with the ext4 filesystem, and mounted it at /data. I then configured /etc/fstab using the filesystem UUID to enable automatic mounting. This helped me understand persistent cloud storage and basic Linux disk management.