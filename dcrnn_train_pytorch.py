from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import yaml


from model.pytorch.dcrnn_supervisor import DCRNNSupervisor
from lib.utils import load_graph_data


def main(args):
    with open(args.config_filename) as f:
        supervisor_config = yaml.load(f)
	
        graph_pkl_filename = supervisor_config['data'].get('graph_pkl_filename')
        sensor_ids, sensor_id_to_ind, adj_mx = load_graph_data(graph_pkl_filename)
        supervisor = DCRNNSupervisor(args.split, args.tval, adj_mx=adj_mx, **supervisor_config)

        supervisor.train()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_filename', default=None, type=str, help='Configuration filename for restoring the model.')
    parser.add_argument('--use_cpu_only', default=False, type=bool, help='Set to true to only use cpu.')
    parser.add_argument('--split',default = 'time',type= str, help = 'The data is split by time or random')
    parser.add_argument('--tval', default = False, type = bool, help= 'Whether to have the data train, tval, val, test(train, val, test, test2)')
    args = parser.parse_args()
    main(args)
