/*
1. Parse command line arguments
2. Get WT310 settings
3. Log parameters (voltage, current, power, and energy) with timestamp to a csv file
*/

#include <iostream>
#include <vector>
#include "settings.h"
#include "parameters.h"
#include "controller.h"
using namespace std;

int main(int argc, char **argv){
	pm_settings wt310_settings;
	pm_parameters wt310_params;
	pm_controller yokogawa;

	/* Edit powermeter settings*/
	wt310_settings.parse_cmd_line(argc, argv);
	wt310_settings.print_settings();

	/* Yokogawa controller*/
	yokogawa.init_ctl(wt310_settings);
	if (wt310_settings.initialize){
		cout << "Elapsed Time:\t" << wt310_settings.elapsed_time() << "seconds" << endl;
		exit(EXIT_SUCCESS);
	}
	yokogawa.integrator_reset();
	yokogawa.integrator_start();
	yokogawa.poll_data(wt310_settings, wt310_params);
	yokogawa.integrator_stop();
	wt310_params.write_csv(wt310_settings.csv_file);

	cout << "Elapsed Time:\t" << wt310_settings.elapsed_time() << "seconds" << endl;

	exit(EXIT_SUCCESS);
}