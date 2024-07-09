import torch

import crypten
import crypten.communicator as comm
import crypten.mpc as mpc
from crypten.mpc import MPCTensor


@mpc.run_multiprocess(world_size=2)
def examine_arithmetic_shares():
    x_enc = crypten.cryptensor([1, 2, 3], ptype=crypten.mpc.arithmetic)
    rank = comm.get().get_rank()
    crypten.print(f"\nRank {rank}:\n {x_enc}\n", in_order=True)


@mpc.run_multiprocess(world_size=2)
def examine_binary_shares():
    x_enc = crypten.cryptensor([2, 3], ptype=crypten.mpc.binary)
    rank = comm.get().get_rank()
    crypten.print(f"\nRank {rank}:\n {x_enc}\n", in_order=True)


@mpc.run_multiprocess(world_size=2)
def examine_conversion():
    x = torch.tensor([1, 2, 3])
    rank = comm.get().get_rank()

    # create an MPCTensor with arithmetic secret sharing
    x_enc_arithmetic = MPCTensor(x, ptype=crypten.mpc.arithmetic)

    # To binary
    x_enc_binary = x_enc_arithmetic.to(crypten.mpc.binary)
    x_from_binary = x_enc_binary.get_plain_text()

    # print only once
    crypten.print("to(crypten.binary):")
    crypten.print(f"  ptype: {x_enc_binary.ptype}\n  plaintext: {x_from_binary}\n")

    # To arithmetic
    x_enc_arithmetic = x_enc_arithmetic.to(crypten.mpc.arithmetic)
    x_from_arithmetic = x_enc_arithmetic.get_plain_text()

    # print only once
    crypten.print("to(crypten.arithmetic):")
    crypten.print(
        f"  ptype: {x_enc_arithmetic.ptype}\n  plaintext: {x_from_arithmetic}\n"
    )
