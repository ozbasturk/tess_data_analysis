#Bu kod test asamasindadir: Selcuk Yalcinkaya
#Asagidaki bilgileri guncelleyip dogrudan calistirabilirsiniz
#kodu calistirmak icin terminal'e 
#python3 TESS_transit_separator.py
#yaziniz
#Eger astropy ile ilgili hata aliyorsaniz asagidaki komut ile yukleyebilirsiniz
#pip3 install astropy
#eger conda kullaniyorsaniz:
#conda install astropy
#komutu ile yukleyebilirsiniz
from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np

#dosya adini giriniz. Ornekte HAT-P-36_TESS_DVT_lc.dat kullanilmistir
dosya=ascii.read('HAT-P-36_TESS_DVT_lc.dat')

time=dosya['time']
flux=dosya['flux']
error=dosya['flux_err']
plt.plot(time,flux,'r.')
plt.show()

#bir sektorde toplam olabilecek transit sayisini asagiya giriniz.
#Bunun icin dvm dosyalarindaki pdf dosyasina bakabilirsiniz
#Sektor ortasindaki boslugu da transit varmis gibi dahil ediniz
#asagidaki ornekte 21 girilmistir
transit_sayisi=21

#dvm pdf dosyasindan period'u giriniz. asagidaki ornekte 1.32735 girilmistir
period=1.32735
#Transit duration (t14) giriniz. Bunun icin elinizdeki en iyi isik egrisinin t14'degerini
#ya da literaturdeki degeri kullanabilirsiniz. Asagidaki ornekte 0.09604 girilmistir
t14=0.09604
#dvm pdf dosyasindaki t0 degerini giriniz. Asagidaki ornekte 1899.4769 girilmistir
t0=1899.4769
print('UYARI: Isik egrileri cizildigi gibi yazdirilmaktadir. Eger kanatlarda yeteri kadar veri yoksa t14 degerini degistiriniz')
print('-----------------------------------------------------------------------------------------------------------------------')
print('t14 dogru olsa bile bazi transitlerin kanatlarinda yeteri kadar veri olmayabilir. Isik egrisinin tamamina bakiniz')
for i in range(transit_sayisi):
    tc=1899.4769+2457000 + period*(i+1)
    maxlim=tc+t14*1.5
    minlim=tc-t14*1.5
    t1=np.where((time > minlim) & (time < maxlim))
    plt.plot(time[t1],flux[t1],'r.')
    plt.show()
    if len(time[t1]) > 20:
        ascii.write([time[t1],flux[t1],error[t1]],'Transit_'+str(i)+'_HAT-P-36_TESS_DVT_lc.dat')
print('UYARI: Olusan dosya sayisi ile gozlenen transit sayisinin esit oldugundan emin olunuz')

    
    







