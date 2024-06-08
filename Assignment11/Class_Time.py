class Time:
    def __init__(self, hh, mm, ss):
        # properties
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()

    # methods
    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)

    def sum(self, other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Time(h_new, m_new, s_new)
        return result

    def sub(self, other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Time(h_new, m_new, s_new)
        return result

    def fix(self):
        if self.second >= 60 :
            self.second -= 60
            self.minute +=1

        if self.minute >= 60 :
            self.minute -= 60
            self.hour +=1

        if self.second < 0 :
            self.second += 60
            self.minute -= 1

        if self.minute < 0 :
            self.minute += 60
            self.hour -= 1

    
    def convert_time_to_seconds(self):
        result = self.hour * 3600 + self.minute * 60 + self.second
        return result

    @staticmethod
    def convert_seconds_to_time(total_seconds):
        h_new = total_seconds // 3600
        m_new = (total_seconds % 3600)// 60
        s_new = total_seconds % 60
        result = Time(h_new, m_new, s_new)
        return result

    def convert_GMT_Tehran(self):
        result =Time(self.hour + 3, self.minute + 30, self.second)
        return result



print("Time 1:")
t1 = Time(3, 45, 33)
t1.show()

print("Time 2:")
t2 = Time(4, 4, 53)
t2.show()

print("The sum of the times")
t3 = t1.sum(t2)
t3.show()

print("Result of Sub:")
t4 = t1.sub(t2)
t4.show()

print("Convert seconds to time:")
seconds = 40000
t5 = Time.convert_seconds_to_time(seconds)
t5.show()

print("Convert time to seconds :")
s = t1.convert_time_to_seconds()
print(s)

print("Convert GMT time to Tehran time :")
t6 = t1.convert_GMT_Tehran()
t6.show()



