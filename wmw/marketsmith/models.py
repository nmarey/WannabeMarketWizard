from django.db import models

# Create your models here.


class IndustryGroups(models.Model):
    symbol = models.CharField(max_length = 10)
    ind_grp_name = models.CharField(max_length = 50, null=True)
    no_of_stocks = models.IntegerField()
    ind_grp_rnk = models.IntegerField()
    ind_grp_rnk_last_wk = models.IntegerField()
    ind_grp_rnk_3_mo = models.IntegerField()
    ind_grp_rnk_6_mo = models.IntegerField()
    pct_chg_ytd = models.DecimalField(max_digits = 6, decimal_places = 2)
    ind_mkt_bal_bil= models.IntegerField()
    dwnld_dt = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

class growth250(models.Model):
    grwth_250_rnk = models.IntegerField()
    symbol = models.CharField(max_length=10)
    co_name = models.CharField(max_length = 50)
    current_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    price_change_usd = models.DecimalField(max_digits = 10, decimal_places = 2)
    price_change_pct = models.DecimalField(max_digits = 5, decimal_places = 1)
    pct_off_high = models.DecimalField(max_digits = 6, decimal_places = 2)
    pct_vol_chg_vs_50 = models.DecimalField(max_digits = 6, decimal_places = 2)
    vol_avg_50_day_shares = models.BigIntegerField()
    vol_avg_50_day_usd = models.BigIntegerField()
    market_cap_mil = models.DecimalField(max_digits=18, decimal_places=1)
    comp_rating = models.IntegerField()
    eps_rating = models.IntegerField()
    rs_rating = models.IntegerField()
    ad_rating = models.CharField(max_length = 10, null=True)
    smr_rating = models.CharField(max_length = 10, null=True)
    ind_grp_rank = models.IntegerField()
    ind_name = models.CharField(max_length = 50) 
    ipo_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    dwnld_dt = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.symbol

