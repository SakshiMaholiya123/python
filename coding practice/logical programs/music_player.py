class Track:
    def __init__(self,song_name,singer,duration):
        self.song_name=song_name
        self.singer=singer
        min,sec=map(int,duration.split(":"))
        self.seconds=min*60+sec

        # def for_dur(self):
        #     return{self.}

        def __str__(self):
            return f"song name is {self.song_name},singer is {self.singer} and the duration is {self.seconds}"

    
class Playlist:
    def __init__(self,playlist_name):
        self.playlist_name=playlist_name
        self.tracks=[]
    
    def add_track(self,track):
        self.tracks.append(track)

    def remove_track(self,track):
        self.tracks.remove(track)
    
    def total_duration(self):
        total=0
        for i in self.track:
            total+=i
        return total
    
    def longest_track(self):
        return max(self.tracks)
    
    def shortest_track(self):
        return min(self.tracks)

    def average_duration(self):
        total=0
        for i in self.seconds:
            total+=i
        avg=total/len(self.seconds)
        return avg
    
    def track_under(self,limit):
        for t in t.seconds:
            if t.seconds<limit:
                return t.song_name

    
    