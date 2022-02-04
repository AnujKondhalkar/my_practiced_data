def designerPdfViewer(h,word):
    # Write your code here
    le=len(word)
    h_l=[]
    for i in range(len(word)):
        h_l.append(h[ord(word[i])-97])
    return max(h_l)*le
h=[1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
word='abc'

print(designerPdfViewer(h,word))
