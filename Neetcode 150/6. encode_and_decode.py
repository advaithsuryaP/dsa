class Solution:

    def __init__(self):
        self.word_length_counter = []

    def encode(self, strs: List[str]) -> str:
        for word in strs:
            self.word_length_counter.append(len(word))
        encoded = ''.join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = list()
        for word_length in self.word_length_counter:
            decoded_word = s[0:word_length]
            decoded.append(decoded_word)
            s = s[word_length:]
        return decoded