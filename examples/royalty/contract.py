from pyteal import *

from beaker.contracts.arcs import ARC18
from beaker.decorators import handler


class MyRoyaltyContract(ARC18):
    @handler
    def create_nft(name: abi.String, *, output: abi.Uint64):
        """Create an nft with a name, to demo subclassing ARC18"""
        return Seq(
            InnerTxnBuilder.Begin(),
            InnerTxnBuilder.SetFields(
                {
                    TxnField.type_enum: TxnType.AssetConfig,
                    TxnField.config_asset_manager: MyRoyaltyContract.address,
                    TxnField.config_asset_name: name.get(),
                    TxnField.config_asset_total: Int(1),
                }
            ),
            InnerTxnBuilder.Submit(),
            output.set(InnerTxn.created_asset_id()),
        )


if __name__ == "__main__":
    mrc = MyRoyaltyContract()
    print(mrc.contract.dictify())