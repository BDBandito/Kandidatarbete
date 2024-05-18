

def specifikationer(x, y):
    # --------------- Specifikationer --------------

    # --------------- Batteri ----------------------
    maxkapacitet_batteri = 30*0.6  # [kWh] *0.6 för att batteriet vill helst inte laddas ur lägre än till 20 % och inte laddar mer än 80%.
    verkningsgrad_batteri = 0.9  # [fraktion]
    startladdning_batteri = 1  # [fraktion]
    #c_tal_batteri =  # [kWh] max urladdningshastighet
    kostnad_batteri = 25000 # [kr] för litiumbatteri

    batteri = [maxkapacitet_batteri, verkningsgrad_batteri, startladdning_batteri, kostnad_batteri]
    batteri_mult = [x * element for element in batteri]
    #litium_batteri =

    # --------------- Vätgaslagring ----------------
    maxkapacitet_H = 8000  # [kWh]
    verkningsgrad_H = 0.4  # [fraktion]
    startladdning_H = 1  # [fraktion]
    kostnad_H = 2000000 # [kr]

    H_lagring = [maxkapacitet_H, verkningsgrad_H, startladdning_H, kostnad_H]
    H_lagring_mult = [y * element for element in H_lagring]

    return batteri_mult, H_lagring_mult

    # --------------- Solpaneler -------------------
    # kostnad_solpanel = 125000 # [kr]


def batteri(inn):
    loss = 0.9
    #stat_loss = (30*3)/100
    #ut = inn*loss-stat_loss
    ut = inn*loss
    return ut

def lagring_H(inn):
    ut = inn*0.4
    return(ut)