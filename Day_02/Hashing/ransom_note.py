#Ransom Note

def ransom_note(magazine,note):
    if len(note)>len(magazine):
        return False
    else:
        freq={}
        for ch in magazine:
            freq[ch]=freq.get(ch,0)+1
        for ch in note:
            if ch not in freq:
                return False
            if freq[ch]>=1:
                freq[ch]-=1
            else:
                return False
        return True

