# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 09:42:44 2022

@author: Usuario
"""

import json
import urllib
import pandas as pd
import numpy

#list of metrics
metric_ids =  ['act.addr.cnt', 'addr.act.rcv.cnt', 'addr.act.sent.cnt', 'addr.bal.0.001.ntv.cnt', 'addr.bal.0.01.ntv.cnt', 'addr.bal.0.1.ntv.cnt', 'addr.bal.1.cnt', 'addr.bal.1.ntv.cnt', 'addr.bal.10.cnt', 'addr.bal.10.ntv.cnt', 'addr.bal.100.cnt', 'addr.bal.100.ntv.cnt', 'addr.bal.100k.cnt', 'addr.bal.100k.ntv.cnt', 'addr.bal.10k.cnt', 'addr.bal.10k.ntv.cnt', 'addr.bal.10m.cnt', 'addr.bal.1k.cnt', 'addr.bal.1k.ntv.cnt', 'addr.bal.1m.cnt', 'addr.bal.1m.ntv.cnt', 'addr.cnt', 'blk.cnt', 'blk.gas.limit.avg', 'blk.hgt', 'blk.int.avg', 'blk.size.byte', 'blk.size.bytes.avg', 'blk.unc.cnt', 'blk.unc.rew', 'blk.unc.rew.ntv', 'blk.unc.rew.pct', 'blk.wght.avg', 'blk.wght.total', 'daily.shp', 'daily.vol', 'diff.avg', 'fees', 'fees.ntv', 'fees.pct.rev', 'hash.rev', 'hash.rev.ntv', 'hashrate', 'hashrate.30d', 'hashrate.rev', 'hashrate.rev.ntv', 'iss.rate', 'iss.rate.day', 'mcap.circ', 'mcap.dom', 'mcap.out', 'mcap.realized', 'min.rev.ntv', 'min.rev.usd', 'miner.1hop.sply', 'miner.1hop.sply.ntv', 'miner.rev.total', 'miner.sply', 'miner.sply.ntv', 'new.iss.ntv', 'new.iss.usd', 'nvt.adj', 'nvt.adj.90d.ma', 'price', 'real.vol', 'reddit.active.users', 'reddit.subscribers', 'rvt.adj', 'rvt.adj.90d.ma', 'sply.act.10y', 'sply.act.180d', 'sply.act.1d', 'sply.act.1y', 'sply.act.2y', 'sply.act.30d', 'sply.act.3y', 'sply.act.4y', 'sply.act.5y', 'sply.act.7d', 'sply.act.90d', 'sply.act.evr', 'sply.act.pct.1y', 'sply.addr.bal.0.001.ntv', 'sply.addr.bal.0.01.ntv', 'sply.addr.bal.0.1.ntv', 'sply.addr.bal.1', 'sply.addr.bal.1.ntv', 'sply.addr.bal.10', 'sply.addr.bal.10.ntv', 'sply.addr.bal.100', 'sply.addr.bal.100.ntv', 'sply.addr.bal.100k', 'sply.addr.bal.100k.ntv', 'sply.addr.bal.10k', 'sply.addr.bal.10k.ntv', 'sply.addr.bal.10m', 'sply.addr.bal.1k', 'sply.addr.bal.1k.ntv', 'sply.addr.bal.1m', 'sply.addr.bal.1m.ntv', 'sply.circ', 'sply.cont.ntv', 'sply.cont.usd', 'sply.out', 'sply.rvv.180d', 'sply.rvv.1y', 'sply.rvv.2y', 'sply.rvv.30d', 'sply.rvv.3y', 'sply.rvv.4y', 'sply.rvv.5y', 'sply.rvv.7d', 'sply.rvv.90d', 'sply.shld', 'sply.top.100', 'sply.top.10pct', 'sply.top.1pct', 'sply.total.iss', 'sply.total.iss.ntv', 'sply.utxo.loss', 'sply.utxo.prof', 'telegram.users', 'twitter.followers', 'txn.cnt', 'txn.cnt.sec', 'txn.cont.call.cnt', 'txn.cont.call.succ.cnt', 'txn.cont.cnt', 'txn.cont.creat.cnt', 'txn.cont.dest.cnt', 'txn.erc20.cnt', 'txn.erc721.cnt', 'txn.fee.avg', 'txn.fee.avg.ntv', 'txn.fee.med', 'txn.fee.med.ntv', 'txn.gas', 'txn.gas.avg', 'txn.gas.limit', 'txn.gas.limit.avg', 'txn.tfr.avg.ntv', 'txn.tfr.erc20.cnt', 'txn.tfr.erc721.cnt', 'txn.tfr.val.adj.ntv', 'txn.tfr.val.med', 'txn.tfr.val.med.ntv', 'txn.tfr.val.ntv', 'txn.tkn.cnt', 'txn.tsfr.cnt', 'txn.tsfr.val.adj', 'txn.tsfr.val.avg', 'txn.vol', 'utxo.age.avg', 'utxo.age.med', 'utxo.age.val.avg', 'utxo.cnt', 'utxo.loss.cnt', 'utxo.prof.cnt']

result = numpy.empty((940,168)) #change number of rows according to size of data by dates, columns = number of metrics
result[:] = numpy.nan

#take initial date as number
day_zero =  1588291200/86400 # 1st may 2020
#day_zero = 1493596800/86400 #1st may 2017
#day_zero = 1525132800/86400 #1st may 2018
#day_zero = 1398902400/86400 #1st may 2014
#day_zero = 1556668800/86400 #1st may 2019


def  getdataf(metrics):
    series = []
    for year in range(20, 23):
        url = "https://data.messari.io/api/v1/assets/ethereum-classic/metrics/%s/time-series?&interval=1d&order=ascending&start=20%s-05-01&end=20%s-05-01" % (metrics, str(year), str(year+1))
        req = urllib.request.Request(url)
        req.add_header('x-messari-api-key', 'your-api-key') #change your-api-key for actual api key
        response = urllib.request.urlopen(req)
        data = json.load(response)["data"]
         
        schema = data["schema"]["values_schema"]
       
        if data["values"] == None:
              continue
       
        series += data["values"]
    return schema, series

def main():
    #data indexed into result array according to date
    
    k = 0
    for metric in metric_ids:
        (variables, vals) = getdataf(metric)
        if len(vals) == 0:
            k = k + 1
            continue
        a = numpy.array(vals)
        days = (a[:,0])/86400000 
        rows = len(days)
        column = len(a[0])
        if column != 2:
            for j,x in zip(range(k, k + column -1), range(1,column)):
                for i in range(0,rows):
                    diff = int(days[i]- day_zero)
                    result[diff,j] = a[i,x] 
            k = k + column - 1
        else:
            for i in range(rows):
                diff = int(days[i]- day_zero)
                result[diff,k] = a[i,1] 
            k += 1
            
    df = pd.DataFrame(result, columns = ['act.addr.cnt', 'addr.act.rcv.cnt', 'addr.act.sent.cnt', 'addr.bal.0.001.ntv.cnt', 'addr.bal.0.01.ntv.cnt', 'addr.bal.0.1.ntv.cnt', 'addr.bal.1.cnt', 'addr.bal.1.ntv.cnt', 'addr.bal.10.cnt', 'addr.bal.10.ntv.cnt', 'addr.bal.100.cnt', 'addr.bal.100.ntv.cnt', 'addr.bal.100k.cnt', 'addr.bal.100k.ntv.cnt', 'addr.bal.10k.cnt', 'addr.bal.10k.ntv.cnt', 'addr.bal.10m.cnt', 'addr.bal.1k.cnt', 'addr.bal.1k.ntv.cnt', 'addr.bal.1m.cnt', 'addr.bal.1m.ntv.cnt', 'addr.cnt', 'blk.cnt', 'blk.gas.limit.avg', 'blk.hgt', 'blk.int.avg', 'blk.size.byte', 'blk.size.bytes.avg', 'blk.unc.cnt', 'blk.unc.rew', 'blk.unc.rew.ntv', 'blk.unc.rew.pct', 'blk.wght.avg', 'blk.wght.total', 'sharpe_30d', 'sharpe_90d','sharpe_1yr','sharpe_3yr','volatility_30d', 'volatility_90d', 'volatility_1yr', 'volatility_3yr','diff.avg', 'fees', 'fees.ntv', 'fees.pct.rev', 'hash.rev', 'hash.rev.ntv', 'hashrate', 'hashrate.30d', 'hashrate.rev', 'hashrate.rev.ntv', 'iss.rate', 'iss.rate.day', 'mcap.circ', 'mcap.dom', 'mcap.out', 'mcap.realized', 'min.rev.ntv', 'min.rev.usd', 'miner.1hop.sply', 'miner.1hop.sply.ntv', 'miner.rev.total', 'miner.sply', 'miner.sply.ntv', 'new.iss.ntv', 'new.iss.usd', 'nvt.adj', 'nvt.adj.90d.ma', 'open', 'high', 'low', 'close', 'volume', 'real.vol', 'reddit.active.users', 'reddit.subscribers', 'rvt.adj', 'rvt.adj.90d.ma', 'sply.act.10y', 'sply.act.180d', 'sply.act.1d', 'sply.act.1y', 'sply.act.2y', 'sply.act.30d', 'sply.act.3y', 'sply.act.4y', 'sply.act.5y', 'sply.act.7d', 'sply.act.90d', 'sply.act.evr', 'sply.act.pct.1y', 'sply.addr.bal.0.001.ntv', 'sply.addr.bal.0.01.ntv', 'sply.addr.bal.0.1.ntv', 'sply.addr.bal.1', 'sply.addr.bal.1.ntv', 'sply.addr.bal.10', 'sply.addr.bal.10.ntv', 'sply.addr.bal.100', 'sply.addr.bal.100.ntv', 'sply.addr.bal.100k', 'sply.addr.bal.100k.ntv', 'sply.addr.bal.10k', 'sply.addr.bal.10k.ntv', 'sply.addr.bal.10m', 'sply.addr.bal.1k', 'sply.addr.bal.1k.ntv', 'sply.addr.bal.1m', 'sply.addr.bal.1m.ntv', 'sply.circ', 'sply.cont.ntv', 'sply.cont.usd', 'sply.out', 'sply.rvv.180d', 'sply.rvv.1y', 'sply.rvv.2y', 'sply.rvv.30d', 'sply.rvv.3y', 'sply.rvv.4y', 'sply.rvv.5y', 'sply.rvv.7d', 'sply.rvv.90d', 'sply.shld', 'sply.top.100', 'sply.top.10pct', 'sply.top.1pct', 'sply.total.iss', 'sply.total.iss.ntv', 'sply.utxo.loss', 'sply.utxo.prof', 'telegram.users', 'twitter.followers', 'txn.cnt', 'txn.cnt.sec', 'txn.cont.call.cnt', 'txn.cont.call.succ.cnt', 'txn.cont.cnt', 'txn.cont.creat.cnt', 'txn.cont.dest.cnt', 'txn.erc20.cnt', 'txn.erc721.cnt', 'txn.fee.avg', 'txn.fee.avg.ntv', 'txn.fee.med', 'txn.fee.med.ntv', 'txn.gas', 'txn.gas.avg', 'txn.gas.limit', 'txn.gas.limit.avg', 'txn.tfr.avg.ntv', 'txn.tfr.erc20.cnt', 'txn.tfr.erc721.cnt', 'txn.tfr.val.adj.ntv', 'txn.tfr.val.med', 'txn.tfr.val.med.ntv', 'txn.tfr.val.ntv', 'txn.tkn.cnt', 'txn.tsfr.cnt', 'txn.tsfr.val.adj', 'txn.tsfr.val.avg', 'txn.vol', 'utxo.age.avg', 'utxo.age.med', 'utxo.age.val.avg', 'utxo.cnt', 'utxo.loss.cnt', 'utxo.prof.cnt'])         
    df.to_excel (r'directory\file_name.xlsx', header=True) #specify directory and file name.
if __name__ == "__main__":
    main()
    
