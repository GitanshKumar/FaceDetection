import collections
import pandas as pd
from PIL import Image
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


def predict(model, X_pred):
    return model.predict([X_pred])


def train():
    df = pd.read_csv('Face Recognition/im_val.csv')

    X = df[["pix0", "pix1", "pix2", "pix3", "pix4", "pix5", "pix6", "pix7", "pix8", "pix9", "pix10", "pix11", "pix12", "pix13", "pix14", "pix15", "pix16", "pix17", "pix18", "pix19", "pix20", "pix21", "pix22", "pix23", "pix24", "pix25", "pix26", "pix27", "pix28", "pix29", "pix30", "pix31", "pix32", "pix33", "pix34", "pix35", "pix36", "pix37", "pix38", "pix39", "pix40", "pix41", "pix42", "pix43", "pix44", "pix45", "pix46", "pix47", "pix48", "pix49", "pix50", "pix51", "pix52", "pix53", "pix54", "pix55", "pix56", "pix57", "pix58", "pix59", "pix60", "pix61", "pix62", "pix63", "pix64", "pix65", "pix66", "pix67", "pix68", "pix69", "pix70", "pix71", "pix72", "pix73", "pix74", "pix75", "pix76", "pix77", "pix78", "pix79", "pix80", "pix81", "pix82", "pix83", "pix84", "pix85", "pix86", "pix87", "pix88", "pix89", "pix90", "pix91", "pix92", "pix93", "pix94", "pix95", "pix96", "pix97", "pix98", "pix99", "pix100", "pix101", "pix102", "pix103", "pix104", "pix105", "pix106", "pix107", "pix108", "pix109", "pix110", "pix111", "pix112", "pix113", "pix114", "pix115", "pix116", "pix117", "pix118", "pix119", "pix120", "pix121", "pix122", "pix123", "pix124", "pix125", "pix126", "pix127", "pix128", "pix129", "pix130", "pix131", "pix132", "pix133", "pix134", "pix135", "pix136", "pix137", "pix138", "pix139", "pix140", "pix141", "pix142", "pix143", "pix144", "pix145", "pix146", "pix147", "pix148", "pix149", "pix150", "pix151", "pix152", "pix153", "pix154", "pix155", "pix156", "pix157", "pix158", "pix159", "pix160", "pix161", "pix162", "pix163", "pix164", "pix165", "pix166", "pix167", "pix168", "pix169", "pix170", "pix171", "pix172", "pix173", "pix174", "pix175", "pix176", "pix177", "pix178", "pix179", "pix180", "pix181", "pix182", "pix183", "pix184", "pix185", "pix186", "pix187", "pix188", "pix189", "pix190", "pix191", "pix192", "pix193", "pix194", "pix195", "pix196", "pix197", "pix198", "pix199", "pix200", "pix201", "pix202", "pix203", "pix204", "pix205", "pix206", "pix207", "pix208", "pix209", "pix210", "pix211", "pix212", "pix213", "pix214", "pix215", "pix216", "pix217", "pix218", "pix219", "pix220", "pix221", "pix222", "pix223", "pix224", "pix225", "pix226", "pix227", "pix228", "pix229", "pix230", "pix231", "pix232", "pix233", "pix234", "pix235", "pix236", "pix237", "pix238", "pix239", "pix240", "pix241", "pix242", "pix243", "pix244", "pix245", "pix246", "pix247", "pix248", "pix249", "pix250", "pix251", "pix252", "pix253", "pix254", "pix255", "pix256", "pix257", "pix258", "pix259", "pix260", "pix261", "pix262", "pix263", "pix264", "pix265", "pix266", "pix267", "pix268", "pix269", "pix270", "pix271", "pix272", "pix273", "pix274", "pix275", "pix276", "pix277", "pix278", "pix279", "pix280", "pix281", "pix282", "pix283", "pix284", "pix285", "pix286", "pix287", "pix288", "pix289", "pix290", "pix291", "pix292", "pix293", "pix294", "pix295", "pix296", "pix297", "pix298", "pix299", "pix300", "pix301", "pix302", "pix303", "pix304", "pix305", "pix306", "pix307", "pix308", "pix309", "pix310", "pix311", "pix312", "pix313", "pix314", "pix315", "pix316", "pix317", "pix318", "pix319", "pix320", "pix321", "pix322", "pix323", "pix324", "pix325", "pix326", "pix327", "pix328", "pix329", "pix330", "pix331", "pix332", "pix333", "pix334", "pix335", "pix336", "pix337", "pix338", "pix339", "pix340", "pix341", "pix342", "pix343", "pix344", "pix345", "pix346", "pix347", "pix348", "pix349", "pix350", "pix351", "pix352", "pix353", "pix354", "pix355", "pix356", "pix357", "pix358", "pix359", "pix360", "pix361", "pix362", "pix363", "pix364", "pix365", "pix366", "pix367", "pix368", "pix369", "pix370", "pix371", "pix372", "pix373", "pix374", "pix375", "pix376", "pix377", "pix378", "pix379", "pix380", "pix381", "pix382", "pix383", "pix384", "pix385", "pix386", "pix387", "pix388", "pix389", "pix390", "pix391", "pix392", "pix393", "pix394", "pix395", "pix396", "pix397", "pix398", "pix399", "pix400", "pix401", "pix402", "pix403", "pix404", "pix405", "pix406", "pix407", "pix408", "pix409", "pix410", "pix411", "pix412", "pix413", "pix414", "pix415", "pix416", "pix417", "pix418", "pix419", "pix420", "pix421", "pix422", "pix423", "pix424", "pix425", "pix426", "pix427", "pix428", "pix429", "pix430", "pix431", "pix432", "pix433", "pix434", "pix435", "pix436", "pix437", "pix438", "pix439", "pix440", "pix441", "pix442", "pix443", "pix444", "pix445", "pix446", "pix447", "pix448", "pix449", "pix450", "pix451", "pix452", "pix453", "pix454", "pix455", "pix456", "pix457", "pix458", "pix459", "pix460", "pix461", "pix462", "pix463", "pix464", "pix465", "pix466", "pix467", "pix468", "pix469", "pix470", "pix471", "pix472", "pix473", "pix474", "pix475", "pix476", "pix477", "pix478", "pix479", "pix480", "pix481", "pix482", "pix483", "pix484", "pix485", "pix486", "pix487", "pix488", "pix489", "pix490", "pix491", "pix492", "pix493", "pix494", "pix495", "pix496", "pix497", "pix498", "pix499", "pix500", "pix501", "pix502", "pix503", "pix504", "pix505", "pix506", "pix507", "pix508", "pix509", "pix510", "pix511", "pix512", "pix513", "pix514", "pix515", "pix516", "pix517", "pix518", "pix519", "pix520", "pix521", "pix522", "pix523", "pix524", "pix525", "pix526", "pix527", "pix528", "pix529", "pix530", "pix531", "pix532", "pix533", "pix534", "pix535", "pix536", "pix537", "pix538", "pix539", "pix540", "pix541", "pix542", "pix543", "pix544", "pix545", "pix546", "pix547", "pix548", "pix549", "pix550", "pix551", "pix552", "pix553", "pix554", "pix555", "pix556", "pix557", "pix558", "pix559", "pix560", "pix561", "pix562", "pix563", "pix564", "pix565", "pix566", "pix567", "pix568", "pix569", "pix570", "pix571", "pix572", "pix573", "pix574", "pix575", "pix576", "pix577", "pix578", "pix579", "pix580", "pix581", "pix582", "pix583", "pix584", "pix585", "pix586", "pix587", "pix588", "pix589", "pix590", "pix591", "pix592", "pix593", "pix594", "pix595", "pix596", "pix597", "pix598", "pix599", "pix600", "pix601", "pix602", "pix603", "pix604", "pix605", "pix606", "pix607", "pix608", "pix609", "pix610", "pix611", "pix612", "pix613", "pix614", "pix615", "pix616", "pix617", "pix618", "pix619", "pix620", "pix621", "pix622", "pix623", "pix624"]].values
    y = df['isface'].values

    #X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = MLPClassifier()
    model.fit(X, y)

    return model, X


def file_data(location):

    img = Image.open(location)
    bw_img = img.convert("L")
    resized_img = bw_img.resize((25,25))
    data = resized_img.getdata()

    return data


if __name__ == "__main__":
    model, X = train()
    X = list(X)

    while True:
        location = input("Enter complete file location [to exit type \"exit\"]: ")
        if location == "exit":
            break
        data = list(file_data(location))

        face = predict(model, data)
        print(face, "1")
        
        present = False
        for elem in X:
            if collections.Counter(elem) == collections.Counter(data):
                present = True
        
        if not present:
            ent = str(data)
            ent = ent[1:len(ent)-1]
            ent = ent.replace(" ", "")

            f = open("Face Recognition/im_val.csv", "a")
            if face == [0]:
                f.write("0,")
                print("True")
            else:
                f.write("1,")
            
            f.write("{}{}".format(ent, "\n"))
            f.close()            