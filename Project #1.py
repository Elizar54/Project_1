import russian_localization as ru

vlm_of_ptrl_in_gllns = float(input(ru.sign_input))
vlm_of_ptrl_in_ltrs = vlm_of_ptrl_in_gllns * 4.54  # Calculating volume of petrol in litres.
vlm_of_CO2 = vlm_of_ptrl_in_gllns * 20 # Calculating volume of CO2 being produced by burning such volume of petrol.
oil_need_to_prdc = vlm_of_ptrl_in_gllns / 19.5 # Calculating volume of oil needed to produce such volume of petrol.
vlm_of_ethnl = vlm_of_ptrl_in_gllns * 115000 / 75700 # Calculating the equal volume of ethanol.
price_in_dollars = vlm_of_ptrl_in_gllns * 3.00 # Calculating the price of such volume of petrol.
annual_ptrl_cons_ru = 745.12 * 1000 * 365 / 0.0063 # Calculating the approximate annual consuption of petrol in Russia.
daily_ptrl_cons_nsk = 0.8 * 1633595 # Calculating the approximate daily consuption of petrol in Novosibirsk.

print(ru.vlm_of_ptrl_in_ltrs, vlm_of_ptrl_in_ltrs)
print(ru.vlm_of_CO2, vlm_of_CO2)
print(ru.oil_need_to_prdc, round(oil_need_to_prdc, 2))
print(ru.vlm_of_ethnl, round(vlm_of_ethnl, 2))
print(ru.price_in_dollars, price_in_dollars)
print(ru.annual_ptrl_cons_ru, round(annual_ptrl_cons_ru, 2))
print(ru.daily_ptrl_cons_nsk, daily_ptrl_cons_nsk)