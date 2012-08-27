import matplotlib.pyplot as plt
from datetime import datetime
import dateutil, pylab
from pylab import *

fig = plt.figure()
fig.suptitle('Sentiment vs. Time by Topic', fontsize=14, fontweight='bold')

#china plot
china = fig.add_subplot(321)
sentiment = [0.0,5.875, 1.25, 1.5, 2.0, 1.625, 3.25, 4.375, 0.125, 1.875, 3.5, 2.125, 1.75, 4.375, 0.0, -0.375, 3.25, -0.125, 2.375, 3.25, 6.625, 3.75, 1.0, 3.125, 0.25, 2.0, 1.5, 0.875, 2.25, 5.5, 0.375, 4.125, -0.125, 1.75, 6.25, 7.25, 4.875,0.0]
date = ['1-Jan-1920','1-Sep-1998', '1-Apr-1934', '1-Jul-1926', '1-Jun-1942', '1-Oct-2003', '1-Oct-2003', '1-May-1998', '1-Jun-2005', '1-Dec-2005', '1-Feb-2006', '1-Mar-2006', '1-Mar-2006', '1-Mar-2006', '1-Apr-2006', '1-May-2006', '1-Nov-2006', '1-Nov-2006', '1-Apr-2007', '1-Jun-2007', '1-Sep-2007', '1-Dec-2007', '1-Jun-2008', '1-Jun-2008', '1-Mar-2009', '1-Jan-2010', '1-Mar-2010', '1-Apr-2010', '1-Jun-2010', '1-Dec-2010', '1-Jun-2011', '1-Jul-1986', '1-Nov-1989', '1-May-1991', '1-Sep-1994', '1-Mar-1997', '1-Sep-1997','1-Dec-2012']
dates = [dateutil.parser.parse(s) for s in date]
#plt.plot(num2date(pylab.date2num(dates)), sentiment, 'ro')
china.stem(num2date(pylab.date2num(dates)), sentiment, linefmt='r-', markerfmt='ko', basefmt='k-')

title('China')
ylabel('Sentiment')
xlabel('Time')
xlim(num2date(pylab.date2num(dateutil.parser.parse('1-Jan-1920'))),num2date(pylab.date2num(dateutil.parser.parse('1-Dec-2012'))))
ylim(-3,12)
date = []
sentiment =[]

#American
american = fig.add_subplot(322)
sentiment = [0.0,0.0, 0.875, 3.5, 4.625, 3.0, 1.875, 4.375, 2.625, 2.0, 1.375, 0.0, 1.25, 0.5, -0.125, 1.375, 1.875, 1.5, 1.75, 0.25, 3.0, 2.875, 1.0, 1.875, -0.5, 0.125, 4.375, 0.0, 0.0, 3.0, 0.0, 3.0, 5.75, 0.0, 0.125, 0.0, -0.25, 0.125, 0.375, 0.25, -0.25, 8.25, 0.0, 0.0, -0.125, -0.125, -0.125, -0.125, 3.25, 0.25, 0.0, 0.375, 6.0, 4.125, 2.125, 5.75, -3.0, 2.875, 5.5,0.0]
date = ['1-Jan-1920','1-Mar-1977', '1-Nov-1977', '1-Mar-1978', '1-Nov-1978', '1-Jul-1980', '1-Jul-1981', '1-Mar-1982', '1-Mar-1982', '1-Jan-1983', '1-Sep-1983', '1-Jan-1984', '1-May-1985', '1-Dec-2001', '1-May-2002', '1-Apr-1924', '1-Jan-1925', '1-Jan-1928', '1-Mar-1961', '1-Nov-1962', '1-Nov-1953', '1-Mar-1954', '1-Mar-1954', '1-Sep-1941', '1-Mar-1944', '1-Jan-1945', '1-Mar-1964', '1-Nov-1984', '1-Nov-1984', '1-Aug-2003', '1-Oct-2003', '1-Oct-2003', '1-Dec-2003', '1-Jul-1976', '1-Mar-2004', '1-Apr-1927', '1-Nov-1977', '1-Nov-1977', '1-Nov-1980', '1-May-1981', '1-Sep-2004', '1-Jan-2001', '1-Mar-2006', '1-Jun-2006', '1-Nov-2006', '1-Jan-1961', '1-Nov-1955', '1-May-1954', '1-Jul-2007', '1-Nov-2009', '1-Dec-2009', '1-Dec-2009', '1-Jan-1985', '1-Nov-1986', '1-Jan-1990', '1-Jan-1990', '1-Sep-1991', '1-Jul-1992', '1-Nov-1996','1-Dec-2012']
dates = [dateutil.parser.parse(s) for s in date]
american.stem(num2date(pylab.date2num(dates)), sentiment, linefmt='b-', markerfmt='ko', basefmt='k-')

title('American')
ylabel('Sentiment')
xlabel('Time')
xlim(num2date(pylab.date2num(dateutil.parser.parse('1-Jan-1920'))),num2date(pylab.date2num(dateutil.parser.parse('1-Dec-2012'))))
ylim(-3,12)
date = []
sentiment =[]

#Japan
#japan = fig.add_subplot(323)
#sentiment = [-0.625, 0.5, 0.875, 0.0, 0.0, 0.0, 1.0, 0.0, 0.125, 0.0, 0.25, 5.875, 0.5]
#date = ['1-Mar-1977', '1-Oct-2002', '1-Dec-2003', '1-Jul-1976', '1-Nov-1981', '1-May-1981', '1-May-1981', '1-Apr-2007', '1-Mar-2009', '1-May-2009', '1-Nov-2009', '1-Sep-1994', '1-Jul-1995']
#dates = [dateutil.parser.parse(s) for s in date]
#japan.stem(num2date(pylab.date2num(dates)), sentiment, linefmt='y-', markerfmt='ko', basefmt='k-')

#title('Japan')
#ylabel('Sentiment')
#xlabel('Time')
#xlim(num2date(pylab.date2num(dateutil.parser.parse('1-Jan-1920'))),num2date(pylab.date2num(dateutil.parser.parse('1-Dec-2012'))))
#ylim(-3,12)
#date = []
#sentiment =[]

#Innovation
innovation = fig.add_subplot(323)
sentiment = [0.0,8.25, 7.375, 5.875, 2.375, 3.625, 6.25, 2.75, 3.375, 3.0, 6.5, 1.875, 5.75, 1.625, -0.125, 3.75, 2.875, 5.125, 11.125, -0.25, 3.625, 5.375, 7.125, 3.0, 0.125, 2.125, 3.625, 6.25, 0.5, 6.25, 7.875, 5.875, 1.75, 7.5, 3.375, 3.25, 9.625, -0.125, -0.375, 5.35, 1.0, -0.125, 0.0, 5.625, 8.75, 0.0, 0.0, 2.75, 5.875, 3.5, 4.875, 7.375, 12, 4.625, 0.125, 6.875, 0.625, 2.375, 0.625, 1.125, 1.25, 0.25, 6.625, 3.875, -0.875, -0.375, 6.125, -0.75, 5.25, 3.375, 4.625, 1.875, 4.875, 0.0, 0.25, 0.0, 8.125, 7.875,0.0]
date = ['1-Jan-1920','1-Nov-1998', '1-May-2000', '1-Jan-1965', '1-Jul-1968', '1-Mar-2001', '1-Mar-2001', '1-May-1962', '1-Aug-2002', '1-Aug-2002', '1-Aug-2002', '1-Aug-2002', '1-Aug-2002', '1-Aug-2002', '1-Aug-2002', '1-Oct-2002', '1-Nov-2002', '1-Mar-2003', '1-Sep-2003', '1-Sep-1981', '1-Apr-2004', '1-Jul-2004', '1-Jul-2004', '1-Oct-2004', '1-Oct-2004', '1-May-2005', '1-Mar-2001', '1-Mar-2001', '1-Nov-2005', '1-Nov-2005', '1-Feb-2006', '1-Mar-2006', '1-Apr-2006', '1-Apr-2006', '1-Apr-2006', '1-May-2006', '1-May-2006', '1-Sep-2006', '1-Sep-2006', '1-Nov-2006', '1-Mar-2007', '1-Nov-2050', '1-Jun-2007', '1-Jun-2007', '1-Jun-2007', '1-Sep-2007', '1-Nov-2007', '1-Dec-2007', '1-Jan-2008', '1-Apr-2008', '1-Nov-2008', '1-Dec-2008', '1-Dec-2008', '1-Dec-2008', '1-Mar-2009', '1-Mar-2009', '1-Sep-2009', '1-Oct-2009', '1-Dec-2009', '1-Dec-2009', '1-Jan-2010', '1-May-2010', '1-Jul-2010', '1-Jul-2010', '1-Sep-2010', '1-Jun-2011', '1-Jun-2011', '1-Jun-2011', '1-Oct-2011', '1-May-1985', '1-Nov-1989', '1-Mar-1990', '1-Sep-1994', '1-Jul-1995', '1-Jul-1995', '1-Jul-1995', '1-Jan-1996', '1-Jul-1997','1-Dec-2012']
dates = [dateutil.parser.parse(s) for s in date]
innovation.stem(num2date(pylab.date2num(dates)), sentiment, linefmt='m-', markerfmt='ko', basefmt='k-')

title('Innovation')
ylabel('Sentiment')
xlabel('Time')
xlim(num2date(pylab.date2num(dateutil.parser.parse('1-Jan-1920'))),num2date(pylab.date2num(dateutil.parser.parse('1-Dec-2012'))))
ylim(-3,12)
date = []
sentiment =[]

#Manufacturing
manufacturing = fig.add_subplot(324)
sentiment = [0.0,1.25, 1.625, 2.625, 2.25, 4.0, 2.5, 0.875, 1.5, 4.0, 3.375, 7.0, 5.625, 4.5, 2.0, 1.0, 4.625, -0.125, 1.875, 2.375, 2.125, 0.375, 0.375, 7.125, -0.25, 2.25, 3.375, 6.625, 6.0, 4.125, 6.5, 8.375, 0.5, 2.625, 4.5, 5.75, 1.25, 2.5, 3.5, 2.625, 4.125, 5.625, 3.75, 5.75, 4.75, 4.75, 7.625, 4.5, 6.5, 3.375, 1.25, 8.25, 7.75, 5.375, 5.5, 1.375,0.0]
date = ['1-Jan-1920','1-Nov-2000', '1-May-1969', '1-Sep-1972', '1-May-1974', '1-Sep-1977', '1-Jan-1978', '1-Sep-1979', '1-Jan-1981', '1-Jul-1981', '1-Mar-1983', '1-Mar-1984', '1-Mar-1987', '1-Sep-1985', '1-Jun-1935', '1-Jan-1925', '1-Jan-1925', '1-Apr-1926', '1-Nov-1959', '1-Nov-1960', '1-Jan-1923', '1-Nov-1988', '1-Nov-1988', '1-Jul-1906', '1-Sep-1954', '1-May-1985', '1-Mar-1986', '1-Nov-1986', '1-May-1986', '1-Nov-1986', '1-Sep-1987', '1-Mar-1987', '1-Sep-1988', '1-Sep-1988', '1-Jul-1988', '1-Jul-1988', '1-Mar-1988', '1-Jan-1989', '1-Jan-1989', '1-Mar-1989', '1-Nov-1988', '1-Jan-1990', '1-May-1990', '1-Nov-1990', '1-Nov-1990', '1-Nov-1990', '1-Jan-1991', '1-Jul-1991', '1-May-1992', '1-May-1992', '1-Jan-1993', '1-Jan-1994', '1-Sep-1994', '1-Sep-1995', '1-May-1997', '1-Nov-1997','1-Dec-2012']
dates = [dateutil.parser.parse(s) for s in date]
manufacturing.stem(num2date(pylab.date2num(dates)), sentiment, linefmt='k-', markerfmt='ko', basefmt='k-')

title('Manufacturing')
ylabel('Sentiment')
xlabel('Time')
xlim(num2date(pylab.date2num(dateutil.parser.parse('1-Jan-1920'))),num2date(pylab.date2num(dateutil.parser.parse('1-Dec-2012'))))
ylim(-3,12)
date = []
sentiment =[]

#Technology
technology = fig.add_subplot(325)
sentiment = [0.0,3.75, 0.75, 2.375, 5.0, 4.875, 1.0, 2.375, 1.0, 0.375, 6.0, 2.5, 2.625, 1.0, 1.625, 0.5, 4.375, 4.625, 0.0, 3.0, 5.25, 0.875, 4.0, 1.75, 1.875, 2.25, 0.5, 0.125, -0.25, 9.375, 5.875, 0.125, 5.625, 6.75, 5.25, 6.0, 1.125, 7.125, 0.625, 0.125, -0.125, 0.0, 1.125, 4.25, 0.0, 1.0, 4.625, 0.0, 3.5, -0.125, 0.875, 0.125, 5.25, 3.375, 4.625, 3.875, 6.5, 5.0, 4.0, 5.875, 4.875, 4.875, 11.875, 4.75, 3.0, 2.375, 3.25, 1.0, 4.75, 1.125, 1.0, 5.625, 4.875, 4.125, 4.125, 6.125,0.0]
date = ['1-Jan-1920','1-Sep-1998', '1-Mar-2000', '1-Mar-2000', '1-Sep-2000', '1-Nov-1969', '1-Nov-1971', '1-Sep-1973', '1-Jan-1974', '1-Jan-1975', '1-Jan-1975', '1-Jul-1980', '1-Mar-1981', '1-Sep-1981', '1-Jan-1982', '1-Jan-1982', '1-Sep-1982', '1-Jan-1983', '1-Jul-1983', '1-Nov-1983', '1-Feb-2001', '1-Jul-1984', '1-May-1984', '1-May-1989', '1-May-2001', '1-Mar-2002', '1-Nov-1961', '1-Jan-1959', '1-Mar-1960', '1-Aug-2002', '1-Nov-2002', '1-Feb-2003', '1-May-2003', '1-Jul-2003', '1-Sep-2003', '1-Oct-2003', '1-Feb-2004', '1-Feb-2004', '1-Mar-2004', '1-Sep-1981', '1-Jan-1981', '1-Jan-1981', '1-Dec-2004', '1-Apr-2005', '1-Mar-1979', '1-Nov-1996', '1-Jan-2006', '1-Jun-2007', '1-Apr-2008', '2-Apr-2008', '1-Jun-2008', '1-Nov-2008', '1-Oct-2011', '1-Jul-1985', '1-Sep-1987', '1-Sep-1988', '1-Nov-1988', '1-Nov-1989', '1-Mar-1990', '1-May-1990', '1-Jul-1990', '1-Jan-1991', '1-Jan-1991', '1-Sep-1991', '1-Sep-1991', '1-Mar-1992', '1-Jul-1992', '1-May-1993', '1-Sep-1993', '1-Nov-1993', '1-Jan-1994', '1-Mar-1995', '1-Sep-1995', '1-May-1997', '1-Jan-1997', '1-Sep-1997','1-Dec-2012']
dates = [dateutil.parser.parse(s) for s in date]
technology.stem(num2date(pylab.date2num(dates)), sentiment, linefmt='c-', markerfmt='ko', basefmt='k-')

title('Technology')
ylabel('Sentiment')
xlabel('Time')
xlim(num2date(pylab.date2num(dateutil.parser.parse('1-Jan-1920'))),num2date(pylab.date2num(dateutil.parser.parse('1-Dec-2012'))))
ylim(-3,12)
date = []
sentiment =[]

#War
war = fig.add_subplot(326)
sentiment = [0.0,0.625, 0.875, 2.75, 0.625, -0.75, 1.5, 1.125, 1.625, 0.375, 1.75, 1.25, 0.75, 2.0, 0.75, 0.25, 2.5, 1.5, 0.375, 2.75, 1.25, 2.375, 1.375, 1.125, 2.375, 3.25, 0.5, 1.75, 3.0, 0.625, 3.5, 2.0, 2.75, 2.0, 0.125, 2.375, 1.375, 0.375, 2.875, 3.375, 1.25, 0.875, 1.0, 0.875, 0.375, 2.625, 0.625, 2.0, 0.5, 3.125, 0.875, 2.0, 0.0, 1.5, 0.625, 1.0, 1.75, 2.25, 0.0, 1.5, 2.375, 2.125, 4.25, -0.875, 0.5, 0.75, 0.875, 2.625, 0.375, 0.625, 0.0, 0.875, 3.125, 4.25, 3.5,0.0]
date = ['1-Jan-1920','1-Jul-1976', '1-May-1989', '1-Oct-1923', '1-Oct-1923', '1-Jan-1932', '1-Jul-1925', '1-Jan-1926', '1-Jan-1931', '1-Apr-1932', '1-Sep-1939', '1-Oct-1930', '1-Oct-1930', '1-Jul-1924', '1-Jul-1924', '1-Nov-1962', '1-Jun-1943', '1-Jan-1947', '1-Jan-1947', '1-Sep-1943', '1-Sep-1943', '1-Sep-1943', '1-Sep-1943', '1-Jun-1946', '1-Mar-1942', '1-Mar-1942', '1-Mar-1942', '1-Mar-1942', '1-Mar-1942', '1-Sep-1946', '1-Jul-1948', '1-Jun-1941', '1-Sep-1940', '1-Sep-1940', '1-Mar-1941', '1-Jan-1942', '1-Jan-1942', '1-Mar-1948', '1-Mar-1948', '1-Sep-1941', '1-Mar-1944', '1-Jan-1941', '1-Mar-1951', '1-Jun-1945', '1-Mar-1943', '1-Mar-1943', '1-Mar-1943', '1-Mar-1943', '1-Mar-1943', '1-Mar-1943', '1-Mar-1943', '1-Jun-1942', '1-Jun-1942', '1-Sep-1942', '1-May-1948', '1-Sep-42', '1-Sep-51', '1-Sep-42', '1-Sep-42', '1-Sep-42', '1-Jun-42', '1-Jun-1942', '1-Jan-1943', '1-Jan-1943', '1-Jan-1943', '1-Jan-1943', '1-Jan-1943', '1-Jul-1951', '1-Oct-1922', '1-May-1986', '1-Apr-1927', '1-Dec-2006', '1-Nov-1992', '1-Jul-1993', '1-Jul-1993','1-Dec-2012']
dates = [dateutil.parser.parse(s) for s in date]
war.stem(num2date(pylab.date2num(dates)), sentiment, linefmt='y-', markerfmt='ko', basefmt='k-')

title('War')
ylabel('Sentiment')
xlabel('Time')
xlim(num2date(pylab.date2num(dateutil.parser.parse('1-Jan-1920'))),num2date(pylab.date2num(dateutil.parser.parse('1-Dec-2012'))))
ylim(-3,12)
date = []
sentiment =[]

plt.show()

