{
	TFile* _fileFoam=new TFile("Silicon_p1mm-Edep.root");
	TFile* _filePb=new TFile("Lead-Edep.root");
	TFile* _filePb_Mirror=new TFile("Lead_Mirror-Edep.root");

	TH1F*histFoam =(TH1F*) _fileFoam->Get("histo");
	TH1F*histLead =(TH1F*) _filePb->Get("histo");
	TH1F*histLead_Mirror =(TH1F*) _filePb_Mirror->Get("histo");

	cout<<"Lead: "<<histLead->Integral()<<endl;
	cout<<"LeadMir: "<<histLead_Mirror->Integral()<<endl;

	cout<<"LeadTotal: "<<histLead->Integral()+histLead_Mirror->Integral()<<endl;
	cout<<"Foam: "<<histFoam->Integral()<<endl;

}
