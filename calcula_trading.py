import pyinputplus

###############################################################
RISKING_AMOUNT = 1
TRADING_AMOUNT = 10
GAIN_RATE = 3/10
comission = 0.04/100
MIN_LEVERAGE = 5

###################################################################
#compra
def buy(opening_price, stop_loss):
    #compra
    shift = (opening_price - stop_loss)/opening_price
    volumen = RISKING_AMOUNT/(shift + comission)
    leverage = volumen / TRADING_AMOUNT

    gain = RISKING_AMOUNT * GAIN_RATE
    gainprice = (gain/volumen + comission) * opening_price + opening_price
    return leverage, gainprice

##########################################################
def buy_risk(opening_price, stop_loss):
    shift = (opening_price - stop_loss)/opening_price
    volumen = MIN_LEVERAGE * TRADING_AMOUNT
    risk = (volumen) * (shift + comission)
    gain = risk * GAIN_RATE
    gainprice = (gain/volumen + comission) * opening_price + opening_price
    return risk, gainprice
######################################################################
def sell(opening_price, stop_loss):
    #venta
    shift = (stop_loss - opening_price)/opening_price
    volumen = RISKING_AMOUNT/(shift + comission)
    leverage = volumen / TRADING_AMOUNT

    gain = RISKING_AMOUNT * GAIN_RATE
    gainprice = opening_price - (gain / volumen + comission) * opening_price
    return leverage, gainprice
##############################################################
def sell_risk(opening_price, stop_loss):
    shift = (stop_loss - opening_price)/opening_price
    volumen = MIN_LEVERAGE * TRADING_AMOUNT
    risk = (volumen) * (shift + comission)
    gain = risk * GAIN_RATE
    gainprice = opening_price - (gain / volumen + comission) * opening_price
    return risk, gainprice
#*********************************************************************#

answer = 'yes'
while answer != 'no':
    opening_price = input ('Introduce precio de apertura: ')
    stop_loss = input ('Introduce el stop loss: ')
    print()

    opening_price = float(opening_price)
    stop_loss = float(stop_loss)

    if opening_price > stop_loss:
        results = buy(opening_price, stop_loss)
    else:
        results = sell(opening_price, stop_loss)

    if results[0] >= 5:
        print(f'Leverage: {results[0]}')
        print(f'Gain Price: {results[1]}')

    elif opening_price > stop_loss:
            results = buy_risk(opening_price, stop_loss)
            print(f'Estarias arriesgando: {results[0]} USDT')
            print(f'Gain Price: {results[1]}')

    elif opening_price < stop_loss:
            results = sell_risk(opening_price, stop_loss)
            print(f'Estarias arriesgando: {results[0]} USDT')
            print(f'Gain Price: {results[1]}')

    answer = pyinputplus.inputYesNo('\nVas a continuar analizando?\n')
    '''
    elif results[0] >= 4.7:
        print('Puedes consederar hacer esta operacion aunque vas a arriesgar un poco mas')
        print(f'Leverage: {results[0]}')
        print(f'Gain Price: {results[1]}')

    else:
        print('Esta oepracion es demasiado riesgosa')
        print(f'El leverage dio {results[0]}')
    '''
