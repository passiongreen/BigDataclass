package JC;

public class TV2 {
    int channel;

    public TV2() {}

    public TV2(int intValue) {
        this.channel = intValue;
    }

    protected void channelUp() {
        channel = channel + 1;

    }

    private void channelDown() {
        channel = channel - 1;
        if (channel <0){
            channel = 0;
        }
    }

    public static void main(String args[]) {
        TV objTV = new TV(11);
        System.out.println("현재 채널은 " + objTV.channel + "번입니다.");
    }


}