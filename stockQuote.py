def stockQuote(scripCode,fdate,fmonth,fyear):
    """
    stockQuote module for Bombay Stock Exchange (BSE) 
    stockQuote(scripCode,fdate,fmonth,fyear)
    fdate = Date of the required Historical Data
    fmonth = Month of the required Historical Data
    fyear = Year of the required Historical Data
    Result in Output.txt in the current Directory
    Eg: 
    >>> import stockQuote
    >>> stockQuote.stockQuote(500010,1,9,2010)
    http://www.bseindia.com/histdata/stockprc2.asp?main1=500010&fdate=1&fmonth=9&fyear=2010&main2=1&default1=1

    """
    import os
    import string
    import urllib
    from xml.dom import minidom
    url = "http://www.google.com/ig/api?stock=%d"% scripCode 
    dom = minidom.parse(urllib.urlopen(url))
    companyNameTag = dom.getElementsByTagName('company')
    companyNameAttributes = companyNameTag[0].attributes['data']
    companyName = companyNameAttributes.nodeValue
    link = "http://www.bseindia.com/histdata/stockprc2.asp?main1=%d" % scripCode+"&fdate=%d" %fdate+"&fmonth=%d"%fmonth+"&fyear=%d"%fyear+"&main2=1&default1=1"
    print link
    orignalPsourceObj = urllib.urlopen(link)
    orignalPsource = orignalPsourceObj.read()
    file = open('Test.txt','w')
    file.write(orignalPsource)
    file.close()
    file = open('Test.txt','r')
    for line in file.readlines():
        line = line.strip()
        txt = "<td align=left width=100px valign=bottom bgcolor=#e6eef1><font face=Arial size=2 color=#ic355d>"
        bool = txt in line
        if  bool == True:
            file1 = open('Test.txt','w')
            file1.write(line)
            file1.close()
    modifiedPsourceObj = open('Test.txt','r')
    text = modifiedPsourceObj.read()
    text = text.strip()
    p = string.replace(text,'<tr><td align=left width=100px valign=bottom bgcolor=#e6eef1><font face=Arial size=2 color=#ic355d>','%s;'%companyName)
    q = string.replace(p,'&nbsp;</font></td><td align=right valign=bottom bgcolor=#e6eef1><font face=Arial size=2 color=#ic355d>',';')
    r = string.replace(q,'&nbsp;</font></td></tr>','\n')
    modifiedPsourceObj.close()
    output = open('Output.txt','a')
    output.write(r)
    output.close()
    os.remove('Test.txt')  
