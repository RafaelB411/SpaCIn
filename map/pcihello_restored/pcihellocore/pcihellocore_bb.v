
module pcihellocore (
	button_external_connection_export,
	hex_display_1_external_connection_export,
	hex_display_2_external_connection_export,
	hexport_external_connection_export,
	inport_external_connection_export,
	led_g_external_connection_export,
	led_r_external_connection_export,
	pcie_hard_ip_0_pcie_rstn_export,
	pcie_hard_ip_0_powerdown_pll_powerdown,
	pcie_hard_ip_0_powerdown_gxb_powerdown,
	pcie_hard_ip_0_refclk_export,
	pcie_hard_ip_0_rx_in_rx_datain_0,
	pcie_hard_ip_0_tx_out_tx_dataout_0,
	switches_external_connection_export);	

	input	[7:0]	button_external_connection_export;
	output	[31:0]	hex_display_1_external_connection_export;
	output	[31:0]	hex_display_2_external_connection_export;
	output	[31:0]	hexport_external_connection_export;
	input	[15:0]	inport_external_connection_export;
	output	[15:0]	led_g_external_connection_export;
	output	[31:0]	led_r_external_connection_export;
	input		pcie_hard_ip_0_pcie_rstn_export;
	input		pcie_hard_ip_0_powerdown_pll_powerdown;
	input		pcie_hard_ip_0_powerdown_gxb_powerdown;
	input		pcie_hard_ip_0_refclk_export;
	input		pcie_hard_ip_0_rx_in_rx_datain_0;
	output		pcie_hard_ip_0_tx_out_tx_dataout_0;
	input	[31:0]	switches_external_connection_export;
endmodule
