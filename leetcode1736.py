class Solution(object):
    def maximumTime(self, time):
        time = list(time)
        
        # Hour tens place
        if time[0] == '?':
            if time[1] == '?' or time[1] <= '3': #if time[1]=='?' and int(time[1])>3:
                time[0] = '2'
            else:
                time[0] = '1'
        
        # Hour units place
        if time[1] == '?':
            if time[0] == '2':
                time[1] = '3'
            else:
                time[1] = '9'
        
        # Minute tens place
        if time[3] == '?':
            time[3] = '5'
        
        # Minute units place
        if time[4] == '?':
            time[4] = '9'
        
        return ''.join(time)
