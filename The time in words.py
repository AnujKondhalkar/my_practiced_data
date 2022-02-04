def timeInWords(h, m):
    # Write your code here
    def num2words(i):
        num_to_text=['one', 'two', 'three', 'four', 'five', 'six',
                       'seven', 'eight', 'nine', 'ten', 'eleven',
                       'twelve', 'thirteen', 'fourteen', 'fifteen',
                       'sixteen','seventeen', 'eighteen', 'nineteen',
                       'twenty', 'twenty one', 'twenty two', 'twenty three',
                       'twenty four', 'twenty five', 'twenty six',
                       'twenty seven', 'twenty eight', 'twenty nine']
        return num_to_text[i-1]
           
    if m<=30:
        if m==00:
            return num2words(h)+" o' clock"
        elif 00<m<15 or 15<m<30:
            p='minute' if m==1 else 'minutes'
            
            return f"{num2words(m)} {p} past "+num2words(h)
        elif m==15:
            return "quarter past "+num2words(h)
        elif m==30:
            return "half past "+num2words(h)
                
    elif m>30 and m!=45 or m>45:
        return f"{num2words(60-m)} minutes to "+num2words(h+1)
    
    elif m==45:
        return "quarter to "+num2words(h+1)
        
if __name__ == '__main__':

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)
    print(result)

