from mysql import DB


class VirtualMachine:

    def __init__(self, id):
        self.db = DB("emmet", "brown", "vmweb")
        sql = "select * from vmachine where id={}".format(id)
        query = self.db.run(sql)
        self.id = id
        self.name = query[0]["name"]
        self.ram = query[0]["ram"]
        self.cpu = query[0]["cpu"]
        self.hdd = query[0]["hdd"]
        self.os = query[0]["os"]

    def stop(self):
        self.set_status(0)
        sql = "delete from process where vmachine_id={}".format(self.id)
        self.db.run(sql)

    def start(self):
        self.set_status(1)

    def suspend(self):
        self.set_status(2)

    def reboot(self):
        self.stop()
        self.start()

    def get_processes(self):
        sql = "select * from process where vmachine_id={} order by pid".\
            format(self.id)
        return self.db.run(sql)

    def run(self, pid, ram, cpu, hdd):
        sql = "insert into process (pid, ram, cpu, hdd, vmachine_id) \
            values({}, {}, {}, {}, {})".format(
            pid,
            ram,
            cpu,
            hdd,
            self.id
        )
        self.db.run(sql)

    def ram_usage(self):
        ram = 0
        for p in self.get_processes():
            ram += p["ram"]
        return ram * 100 / self.ram

    def cpu_usage(self):
        cpu = 0
        for p in self.get_processes():
            cpu += p["cpu"]
        return cpu * 100 / self.cpu

    def hdd_usage(self):
        hdd = 0
        for p in self.get_processes():
            hdd += p["hdd"]
        return hdd * 100 / self.hdd

    def set_status(self, new_status):
        sql = "update vmachine set status={} where id={}".format(
            new_status,
            self.id
        )
        self.db.run(sql)

    def get_status(self):
        sql = "select status from vmachine where id={}".format(self.id)
        r = self.db.run(sql)
        status = r[0]["status"]
        if status == 0:
            return "Stopped"
        elif status == 1:
            return "Running"
        elif status == 2:
            return "Suspended"
